import logging
import os
from PySide import QtCore
from opencloudrender.pathUtils import validate_file_path, add_padding_to_image_path
from opencloudrender.vrayUtils import get_vrscene_dependencies, get_vray_settings
import s3IO

class SyncAssetsThread(QtCore.QThread):
    # thx to those guys I made threading work ;)
    # http://stackoverflow.com/questions/20657753/python-pyside-and-progress-bar-threading
    # http://www.matteomattei.com/pyside-signals-and-slots-with-qthread-example/

    update_progress_signal = QtCore.Signal( str , int , int ) #create a custom signal we can subscribe to to emit update commands
    increment_progress_signal = QtCore.Signal( float ) #create a custom signal we can subscribe to to emit update commands
    update_status_signal = QtCore.Signal( str ) #create a custom signal we can subscribe to to emit update commands
    scene_synced_signal = QtCore.Signal( str )

    def __init__(self, scene_data_list , data_bucket_name ):
        super(SyncAssetsThread,self).__init__()
        self.exiting = False
        self.scene_data_list = scene_data_list
        logging.debug( "SyncAssetsThread - scene_data_list" )
        logging.debug( self.scene_data_list )
        self.data_bucket_name = data_bucket_name

    def run( self ):
        self.update_status_signal.emit( 'Start syncing assets to S3...')
        for scene in self.scene_data_list:
            #convert uploadWithDependencies to an object for cancel funcion
            scene_path = scene[0]
            scene_basename=os.path.basename( scene_path )
            logging.debug( 'scene_path: ' + scene_path )
            ret = 0
            progress_current = 0

            if scene_path.endswith('.vrscene'):
                dependencies = get_vrscene_dependencies( scene_path )
            elif scene_path.endswith('.ass'):
                dependencies = getAssDependencies( scene_path )
            elif scene_path.endswith('.ifd'):
                dependencies = getIFDDependencies( scene_path )

            progress_100 = len( dependencies )+1
            self.update_progress_signal.emit( 'Syncing scene: ' + scene_path , progress_current , progress_100 )

            for asset in dependencies:
                if self.exiting==False:
                    if s3IO.upload_file( self.data_bucket_name , asset ) != 0: # todo make upload a thread for cancel functionality and see if we can finally implement fine grained progress (make the callback a function in the thread object and emit a signal
                        ret=1
                    progress_current=progress_current+1
                    self.update_progress_signal.emit( scene_basename + ' : ' + os.path.basename( asset ) , progress_current , progress_100 )
                else:
                    self.update_progress_signal.emit( scene_basename + ' : sync canceled by user' , progress_current , progress_100 )
                    return 2 #user abort

            if s3IO.upload_file( self.data_bucket_name , scene_path ) != 0:
                ret=1

            progress_current=progress_current+1
            self.update_progress_signal.emit( scene_path , progress_current , progress_100 )


            if ret != 0:
                self.update_status_signal.emit( "Warning: Done syncing assets, but some assets could not be uploaded!'" )
                # todo popup dialog
            else:
                self.update_status_signal.emit( "Done syncing assets to S3..." )
                self.scene_synced_signal.emit( scene_path )

    @QtCore.Slot()
    def cancel(self):
        self.exiting = True

class SyncImagesThread(QtCore.QThread):
    # thx to those guys i mad threading work ;)
    # http://stackoverflow.com/questions/20657753/python-pyside-and-progress-bar-threading
    # http://www.matteomattei.com/pyside-signals-and-slots-with-qthread-example/

    update_progress_signal = QtCore.Signal( str , int , int ) #create a custom signal we can subscribe to to emit update commands

    def __init__(self, scene_data_list , data_bucket_name ):
        super(SyncImagesThread,self).__init__()
        self.exiting = False
        self.scene_data_list = scene_data_list
        self.data_bucket_name = data_bucket_name

    def run( self ):
        self.update_progress_signal.emit( 'Start syncing images from S3...' , 0 , 1 )
        for scene in self.scene_data_list:
            #opencloudrender.download_image_s3( self.ui.dataBucketName.text() , scene[0] , progress_bar=self.ui.progressBar )
            # get outout images from vrscene
            # download them from s3
            scene_path = scene[0]
            vray_settings = get_vray_settings( scene_path )
            output_image_path='/'.join( [ validate_file_path( vray_settings[ "img_dir" ] ) , vray_settings[ "img_file" ]  ] )
            padding = vray_settings[ "anim_frame_padding" ]
            start_frame = int(vray_settings['anim_start'])
            end_frame   = int(vray_settings['anim_end'])

            frame_list = []
            for frame_number in range( start_frame , end_frame+1 , 1 ):
                # todo add a listen mode to keep downloading new files as they appear and exit when all files are finished
                file_path_frame  = add_padding_to_image_path( output_image_path , padding ) % frame_number
                frame_list.append( validate_file_path( file_path_frame ) )
            s3IO.download_files( self.data_bucket_name , frame_list , update_progress_signal=self.update_progress_signal )

        self.update_progress_signal.emit( "Done syncing images from S3..." , 1 , 1 )

    @QtCore.Slot()
    def cancel(self):
        self.exiting = True


"""
def download_image_s3( data_bucket_name , scene_path , progress_bar=None , listen=False ):
"""




def getAssDependencies( ass_path ): # todo implement ARNOLD .ass parsing
    return None

def getIFDDependencies( ass_path ): # todo implement HOUDINI .ifd parsing
    return None