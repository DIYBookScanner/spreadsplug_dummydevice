# -*- coding: utf-8 -*-
import logging
import shutil
import time

from spreads.plugin import DevicePlugin, DeviceFeatures, HookPlugin
from spreads.vendor.pathlib import Path

num_instances = 0

TEST_IMGS = {'even': Path('/home/jojo/clitest1/raw/000.jpg'),
             'odd':  Path('/home/jojo/clitest1/raw/001.jpg')}

class DummyDevicePlugin(DevicePlugin):
    """ Plugin for DummyDevice

    """
    
    def __init__(self, config, device):
        global num_instances
        self.target_page = 'odd' if num_instances == 1 else 'even'
        num_instances += 1
        self.logger = logging.getLogger(
            'DummyDevice[{0}]'.format(self.target_page))
        self.logger.debug("Instantiation completed.")
    
    @classmethod
    def configuration_template(cls):
        """ Allows a plugin to define its configuration keys.

        The returned dictionary has to be flat (i.e. no nested dicts)
        and contain a PluginOption object for each key.

        Example::

          {
           'a_setting': PluginOption(value='default_value'),
           'another_setting': PluginOption(value=[1, 2, 3],
                                           docstring="A list of things"),
           # In this case, 'full-fat' would be the default value
           'milk': PluginOption(value=('full-fat', 'skim'),
                                docstring="Type of milk",
                                selectable=True),
          }

        :return: dict with unicode: PluginOption(value, docstring, selection)
        """
        return {}

    features = (DeviceFeatures.PREVIEW, DeviceFeatures.IS_CAMERA)
    
    @classmethod
    def yield_devices(cls, config):
        """ Search for usable devices, yield one at a time
        
        :param config:  spreads configuration
        :type config:   spreads.confit.ConfigView
        """
        def match():
            if num_instances < 2:
                return True
            else:
                return False
          
        for i in range(2):
            if match():
                yield 'A dummy device'
    
    def set_target_page(self, target_page):
        """ Set the device target page, if applicable.

        :param target_page: The target page
        :type target_page:  unicode in (u"odd", u"even")

        """
        self.target_page = target_page
    
    def prepare_capture(self, path):
        """ Prepare device for scanning.

        What this means exactly is up to the implementation and the type,
        of device, usually it involves things like switching into record
        mode, path and applying all relevant settings.

        :param path:    Project base path
        :type path:     pathlib.Path

        """
        self.logger.info("Preparing capture for path '{0}'".format(path))
    
    def capture(self, path):
        """ Capture a single image with the device.

        :param path:    Path for the image
        :type path:     pathlib.Path

        """
        time.sleep(0.05)
        shutil.copyfile(unicode(TEST_IMGS[self.target_page]),
                        unicode(path)+".jpg")
        self.logger.info("Capturing image into '{0}'".format(path))
