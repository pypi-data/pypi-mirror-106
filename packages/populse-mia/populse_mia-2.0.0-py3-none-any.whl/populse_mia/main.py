# -*- coding: utf-8 -*- #
"""The first module used at the runtime of mia.

Basically, this module is dedicated to the initialisation of the basic
parameters and the various checks necessary for a successful launch of the
mia's GUI.

:Contains:
    :Class:
        - PackagesInstall

    :Function:
        - launch_mia
        - main
        - verify_processes

"""

###############################################################################
# Populse_mia - Copyright (C) IRMaGe/CEA, 2018
# Distributed under the terms of the CeCILL license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html
# for details.
###############################################################################

import copy
import inspect
import os
import pkgutil
import sys
import yaml
from functools import partial
from packaging import version

# PyQt5 imports
from PyQt5.QtCore import QDir, QLockFile, Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QLabel,
                             QFileDialog, QVBoxLayout, QHBoxLayout, QLineEdit)

pypath = []

if 'NO_ET' not in os.environ:
    os.environ['NO_ET'] = "1" # disables any etelemetry check.

# Adding populse_mia path to the sys.path if in developer mode
if not os.path.dirname(os.path.dirname(
        os.path.realpath(__file__))) in sys.path:           # "developer" mode
    DEV_MODE = True
    root_dev_dir = os.path.dirname(
                     os.path.dirname(
                       os.path.dirname(
                         os.path.dirname(os.path.realpath(__file__)))))

    # Note: The following syntax can also be used:
    #root_dev_dir = os.path.abspath(os.path.join('__file__',
    #                                            os.path.pardir,
    #                                            os.path.pardir,
    #                                            os.path.pardir,
    #                                            os.path.pardir))

    branch = ''
    populse_bdir = ''
    capsul_bdir = ''
    soma_bdir = ''

    if not os.path.isdir(os.path.join(root_dev_dir, 'populse_mia')):
        # different sources layout - try casa_distro mode
        root_dev_dir = os.path.dirname(
                     os.path.dirname(
                       os.path.dirname(
                         os.path.dirname(os.path.dirname(__file__)))))
        if os.path.basename(root_dev_dir) == 'populse':
            root_dev_dir = os.path.dirname(root_dev_dir)
            populse_bdir = 'populse'
            soma_bdir = 'soma'
        print('root_dev_dir:', root_dev_dir)
        branch = os.path.basename(os.path.dirname(
                     os.path.dirname(
                       os.path.dirname(__file__))))
        print('branch:', branch)

    i = 0
    # Adding populse_mia
    print('\n- Mia in "developer" mode')
    mia_dev_dir = os.path.join(root_dev_dir, populse_bdir, 'populse_mia',
                               branch, 'python')
    print('  . Using populse_mia package from {} ...'.format(mia_dev_dir))
    sys.path.insert(i, mia_dev_dir)
    pypath.append(mia_dev_dir)
    del mia_dev_dir
    from populse_mia import info
    print(f"    populse_mia version : {info.__version__}")

    # Adding capsul
    if os.path.isdir(os.path.join(root_dev_dir, capsul_bdir, 'capsul')):
        i += 1
        capsul_dev_dir = os.path.join(root_dev_dir, capsul_bdir, 'capsul',
                                      branch)
        print('  . Using capsul package from {} ...'.format(capsul_dev_dir))
        sys.path.insert(i, capsul_dev_dir)
        pypath.append(capsul_dev_dir)
        del capsul_dev_dir

    else:
        import capsul
        capsul_dir = os.path.dirname(os.path.dirname(capsul.__file__))
        print('  . Using capsul package from {} ...'.format(capsul_dir))
        del capsul_dir
        del capsul

     # Adding soma_base:
    if os.path.isdir(os.path.join(root_dev_dir, soma_bdir, 'soma-base')):
        i += 1
        soma_b_dev_dir = os.path.join(root_dev_dir, soma_bdir, 'soma-base',
                                      branch, 'python')
        print('  . Using soma package from {} ...'.format(soma_b_dev_dir))
        sys.path.insert(i, soma_b_dev_dir)
        pypath.append(soma_b_dev_dir)
        del soma_b_dev_dir

    else:
        import soma
        soma_b_dir = os.path.dirname(os.path.dirname(soma.__file__))
        print('  . Using soma package from {} ...'.format(soma_b_dir))
        del soma_b_dir
        del soma

    # Adding soma_workflow:
    if os.path.isdir(os.path.join(root_dev_dir, soma_bdir, 'soma-workflow')):
        i += 1
        soma_w_dev_dir = os.path.join(root_dev_dir, soma_bdir, 'soma-workflow',
                                      branch, 'python')
        print('  . Using soma_workflow package from {} '
              '...'.format(soma_w_dev_dir))
        sys.path.insert(i, soma_w_dev_dir)
        pypath.append(soma_w_dev_dir)
        del soma_w_dev_dir

    else:
        import soma_workflow
        soma_w_dir = os.path.dirname(os.path.dirname(soma_workflow.__file__))
        print('  . Using soma_worflow package from {} ...'.format(soma_w_dir))
        del soma_w_dir
        del soma_workflow

    # Adding populse_db:
    if os.path.isdir(os.path.join(root_dev_dir, populse_bdir, 'populse_db')):
        i += 1
        populse_db_dev_dir = os.path.join(root_dev_dir, populse_bdir,
                                          'populse_db', branch, 'python')
        print('  . Using populse_db package from {} '
              '...'.format(populse_db_dev_dir))
        sys.path.insert(i, populse_db_dev_dir)
        pypath.append(populse_db_dev_dir)
        del populse_db_dev_dir

    else:
        import populse_db
        populse_db_dir = os.path.dirname(os.path.dirname(populse_db.__file__))
        print('  . Using populse_db package from {} ...'.format(populse_db_dir))
        del populse_db_dir
        del populse_db

    # Adding mia_processes:
    if os.path.isdir(os.path.join(root_dev_dir, populse_bdir,
                                  'mia_processes')):
        i += 1
        mia_processes_dev_dir = os.path.join(root_dev_dir, populse_bdir,
                                             'mia_processes', branch, 'python')
        print('  . Using mia_processes package from {} '
              '...'.format(mia_processes_dev_dir))
        sys.path.insert(i, mia_processes_dev_dir)
        pypath.append(mia_processes_dev_dir)
        del mia_processes_dev_dir

    else:

        try:
            import mia_processes

        except Exception:
            pass

        else:
            mia_processes_dir = os.path.dirname(
                                        os.path.dirname(mia_processes.__file__))
            print('  . Using mia_processes package from {} '
                  '...'.format(mia_processes_dir))
            del mia_processes_dir
            del mia_processes

    # Adding personal libraries (User_processes : by default in Mia, but others
    # can be added by developers):
    # FIXME: The same fix type will certainly have to be made in user
    # mode (for ~/.populse_mia/process' ).
    mia_proc = os.path.join(root_dev_dir, populse_bdir,
                                'populse_mia', 'processes')
    
    if os.path.isdir(mia_proc):
        mia_proc_dir = os.listdir(mia_proc)

        if mia_proc_dir:
            i += 1
            sys.path.insert(i, mia_proc)
            pypath.append(mia_proc)
             
            for elt in mia_proc_dir:
                print('  . Using {0} package from {1}...'.format(elt, mia_proc))

        del mia_proc_dir
        del elt

    del mia_proc
    del root_dev_dir

elif 'CASA_DISTRO' in os.environ:
    # If the casa distro developpement environment is detected,
    # developer mode is activated.
    DEV_MODE = True

else:  # "user" mode
    DEV_MODE = False
    print('\n- Mia in "user" mode')

# capsul imports
from capsul.api import get_process_instance

# soma-base imports
from soma.qt_gui.qt_backend.Qt import QMessageBox
from soma.qt_gui.qtThread import QtThreadCall

# populse_mia imports
from populse_mia.user_interface.main_window import MainWindow
from populse_mia.data_manager.project import Project
from populse_mia.software_properties import Config
# from populse_mia.software_properties import verCmp
from populse_mia.data_manager.project_properties import SavedProjects
import capsul.api as capsul_api

main_window = None


class PackagesInstall:
    """Help to make available a pipeline package in the mia pipeline library,
in a recursive way.

    :Contains:
        :Method:
            - __init__
            - add_package

    """

    def __init__(self):
        """Initialise the packages instance attribute."""

        self.packages = {}

    def add_package(self, module_name, class_name=None):
        """Provide recursive representation of a package and its
subpackages/modules, to construct the mia's pipeline library.

        :Parameters:
            - :module_name: name of the module to add in the pipeline
               library
            - :class_name: only this pipeline will be add to the pipeline
               library (optional)

        :returns: dictionary of dictionaries containing
           package/subpackages/pipelines status.
           ex: {package: {subpackage: {pipeline: 'process_enabled'}}}

        """

        if module_name:

            # reloading the package
            if module_name in sys.modules.keys():
                del sys.modules[module_name]

            try:
                __import__(module_name)
                pkg = sys.modules[module_name]

                for k, v in sorted(list(pkg.__dict__.items())):

                    if class_name and k != class_name:
                        continue

                    # checking each class in the package
                    if inspect.isclass(v):

                        try:
                            try:
                                get_process_instance(
                                    '%s.%s' % (module_name, v.__name__))
                            except:
                                if (v is capsul_api.Node
                                    or not issubclass(v, capsul_api.Node)):
                                    raise
                            # updating the tree's dictionary
                            path_list = module_name.split('.')
                            path_list.append(k)
                            pkg_iter = self.packages

                            for element in path_list:

                                if element in pkg_iter.keys():
                                    pkg_iter = pkg_iter[element]

                                else:

                                    if element is path_list[-1]:
                                        pkg_iter[element] = 'process_enabled'
                                        print('Detected brick: ', element)

                                    else:
                                        pkg_iter[element] = {}
                                        pkg_iter = pkg_iter[element]

                        except Exception:
                            pass

                # check if there are subpackages, in this case explore them
                path = getattr(pkg, '__path__', None)
                if path is None and hasattr(pkg, '__file__') and os.path.basename(pkg.__file__).startswith('__init__.'):
                    path = [os.path.dirname(pkg.__file__)]


                if path:
                    for _, modname, ispkg in pkgutil.iter_modules(path):

                        print('\nExploring subpackages of {0}: {1} ...'
                              .format(module_name,
                                      str(module_name + '.' + modname)))
                        self.add_package(str(module_name + '.' + modname),
                                        class_name)

            except ImportError as e:
                print('\nWhen attempting to add a package and its modules to '
                      'the package tree, the following exception was caught:')
                print('{0}'.format(e))

            return self.packages


def launch_mia():
    """Actual launch of the mia software.

    Overload the sys.excepthook handler with the _my_excepthook private
    function. Check if the software is already opened in another instance.
    If not, the list of opened projects is cleared. Checks if saved projects
    known in the mia software still exist, and updates if necessary.
    Instantiates a 'project' object that handles projects and their
    associated database anf finally launch of the mia's GUI.


    **Contains: Private function:**
        - *_my_excepthook(etype, evalue, tback)*
           Log all uncaught exceptions in non-interactive mode.

           All python exceptions are handled by function, stored in
           sys.excepthook. By overloading the sys.excepthook handler with
           _my_excepthook function, this last function is called whenever
           there is a unhandled exception (so one that exits the interpreter).
           We take advantage of it to clean up mia software before closing.

            :Parameters:
                - :etype: exception class
                - :evalue: exception instance
                - :tback: traceback object

            **Contains: Private function:**
              - *_clean_up()*
                 Cleans up the mia software during "normal" closing.

                 Make a clean up of the opened projects just before exiting
                 mia.
        - *_verify_saved_projects()*
               Verify if the projects saved in saved_projects.yml are still
               on the disk.

               :Returns: the list of the deleted projects

    """

    def _my_excepthook(etype, evalue, tback):

        def _clean_up():

            global main_window
            config = Config()
            opened_projects = config.get_opened_projects()

            try:
                opened_projects.remove(main_window.project.folder)
                config.set_opened_projects(opened_projects)
                main_window.remove_raw_files_useless()

            except AttributeError as e:
                opened_projects = []
                config.set_opened_projects(opened_projects)

            print("\nClean up before closing mia done ...\n")

        # log the exception here
        print("\nException hooking in progress ...")
        _clean_up()
        # then call the default handler
        sys.__excepthook__(etype, evalue, tback)
        # there was some issue/error/problem, so exiting
        sys.exit(1)

    def _verify_saved_projects():

        saved_projects_object = SavedProjects()
        saved_projects_list = copy.deepcopy(saved_projects_object.pathsList)
        deleted_projects = []
        for saved_project in saved_projects_list:
            if not os.path.isdir(saved_project):
                deleted_projects.append(os.path.abspath(saved_project))
                saved_projects_object.removeSavedProject(saved_project)

        return deleted_projects

    global main_window
    app = QApplication(sys.argv)
    QApplication.setOverrideCursor(Qt.WaitCursor)
    sys.excepthook = _my_excepthook

    # working from the scripts directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    lock_file = QLockFile(QDir.temp().absoluteFilePath(
        'lock_file_populse_mia.lock'))

    if not lock_file.tryLock(100):
        # software already opened in another instance
        pass

    else:
        # no instances of the software is opened, the list of opened projects
        # can be cleared
        config = Config()
        config.set_opened_projects([])

    deleted_projects = _verify_saved_projects()
    project = Project(None, True)
    main_window = MainWindow(project, deleted_projects=deleted_projects)
    main_window.show()

    # make sure to instantiate the QtThreadCall singleton from the main thread
    qt_thread_call = QtThreadCall()

    app.exec()


def check_python_version():
    if sys.version_info[:2] < (3, 5):
        raise AssertionError("The populse_mia is ensured to work with Python "
                             ">= 3.5")


def main():
    """Make basic configuration check then actual launch of mia.

    Checks if MIA is called from the site/dist packages (user mode) or from a
    cloned git repository (developer mode). Tries to update the dev_mode
    parameter accordingly and the mia_path if necessary, in the
    ~/.populse_mia/configuration.yml file (this file must be available from
    the ~/.populse_mia directory). Launches the verify_processes()
    function, then the launch_mia() function (mia's real launch !!). When
    mia is exited, if the ~/.populse_mia/configuration.yml exists, sets the
    dev_mode parameter to False.

    - If launched from a cloned git repository ('developer mode'):
        - if the ~/.populse_mia/configuration.yml exists, updates
          the dev_mode parameter to True
        - if the ~/.populse_mia/configuration.yml is not existing
          nothing is done (in developer mode, the mia_path is the
          cloned git repository.
    - If launched from the site/dist packages ('user mode'):
        - if the ~/.populse_mia/configuration.yml exists, updates
          the dev_mode parameter to False and, if not found, update
          the mia_path parameter.
        - if the file ~/.populse_mia/configuration.yml file does
          not exist or if the returned mia_path parameter is incorrect, a
          valid mia_path path is requested from the user, in order
          to try to fix a corruption of this file.

    :Contains:
        :Private function:
            - *_browse_mia_path()*
                The user define the mia_path parameter.

                This method, used only if the mia configuration parameters are
                not accessible, goes with the _verify_miaConfig function,
                which
                will use the value of the mia_path parameter, defined here.

                :Parameters dialog: QtWidgets.QDialog object ('msg' in the main
                   function)

            - *_verify_miaConfig()*

                The purpose of this method is twofold. First, it allows to
                update the obsolete values for some parameters of the
                mia_user_path/properties/config.yml file. Secondly, it allows
                to correct the value of the mia_user_path parameter in the
                ~/.populse_mia/configuration.yml file, (in the case of a user
                mode launch, because the developer mode launch does not need
                this parameter).

                In the case of a launch in user mode, this method goes with the
                _browse_mia_path() function, the latter having allowed the
                definition of the mia_user_path parameter, the objective here
                is to check if the value of this parameter is valid. The
                dev_mode=False and mia_path parameters are saved in the
                ~/.populse_mia/configuration.yml file (the mia_user_path
                parameter is mandatory in the user mode). Then the data in the
                mia_path/properties/config.yml file are checked. If an
                exception
                is raised during the  _verify_miaConfig function, the "MIA path
                selection" window is not closed and the user is prompted again
                to set the mia_user_path parameter.

                :Parameters dialog: QtWidgets.QDialog object ('msg' in the main
                   function)

    """

    def _browse_mia_path(dialog):

        dname = QFileDialog.getExistingDirectory(dialog,
                                                 "Please select MIA path",
                                                 os.path.expanduser('~'))
        dialog.file_line_edit.setText(dname)

    def _verify_miaConfig(dialog=None):

        save_flag = False

        if DEV_MODE:                     # "developer" mode

            try:
                config = Config()
                if not config.get_admin_hash():
                    config.set_admin_hash(
                        "60cfd1916033576b0f2368603fe612fb"
                        "78b8c20e4f5ad9cf39c9cf7e912dd282")
            except Exception as e:
                print('\nMIA configuration settings could not be '
                      'recovered: {0} ...'.format(e))
                print('\nMIA is exiting ...\n')
                sys.exit(1)

        elif dialog is not None:  # "user" mode only if problem

            mia_home_config = dict()
            mia_home_config["dev_mode"] = False
            mia_home_config["mia_user_path"] = dialog.file_line_edit.text()
            print('\nNew values in ~/.populse_mia/configuration.yml: ')

            for key, value in mia_home_config.items():
                print('- {0}: {1}'.format(key, value))

            print()

            with open(dot_mia_config, 'w', encoding='utf8') as configfile:
                yaml.dump(mia_home_config, configfile,
                          default_flow_style=False,
                          allow_unicode=True)

            try:
                config = Config()
                if not config.get_admin_hash():
                    config.set_admin_hash(
                        "60cfd1916033576b0f2368603fe612fb"
                        "78b8c20e4f5ad9cf39c9cf7e912dd282")
                dialog.close()

            except Exception as e:
                print('\nCould not fetch the '
                      'configuration file: {0} ...'.format(e, ))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("populse_mia - Error: "
                                   "mia path directory incorrect")
                msg.setText("Error: Please select the MIA path (directory with"
                            "\nthe processes, properties & resources "
                            "directories): ")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.buttonClicked.connect(msg.close)
                msg.exec()

        else:  # "user" mode (initial pass)
            config = Config()
            if not config.get_admin_hash():
                config.set_admin_hash(
                    "60cfd1916033576b0f2368603fe612fb"
                    "78b8c20e4f5ad9cf39c9cf7e912dd282")

        if 'config' in locals():

            for key, value in config.config.items():

                if value == 'no':
                    save_flag = True
                    config.config[key] = False

                if value == 'yes':
                    save_flag = True
                    config.config[key] = True

                if save_flag is True:
                    config.saveConfig()

    dot_mia_config = os.path.join(os.path.expanduser("~"), ".populse_mia",
                                  "configuration.yml")

    if DEV_MODE:                         # "developer" mode

        if os.path.isfile(dot_mia_config):
            print('\n{0} has been detected.'.format(dot_mia_config))

            with open(dot_mia_config, 'r') as stream:

                if version.parse(yaml.__version__) > version.parse("5.1"):
                    mia_home_config = yaml.load(stream,
                                                Loader=yaml.FullLoader)
                else:
                    mia_home_config = yaml.load(stream)

            mia_home_config["dev_mode"] = True

            with open(dot_mia_config, 'w', encoding='utf8') as configfile:
                yaml.dump(mia_home_config,
                          configfile,
                          default_flow_style=False,
                          allow_unicode=True)

        else:
            print('\n{0} has not been detected.'.format(dot_mia_config))

        _verify_miaConfig()

    else:  # "user" mode

        try:
            if not os.path.exists(os.path.dirname(dot_mia_config)):
                os.mkdir(os.path.dirname(dot_mia_config))
                print('\nThe {0} directory is created '
                      '...'.format(os.path.dirname(dot_mia_config)))

            with open(dot_mia_config, 'r') as stream:

                if version.parse(yaml.__version__) > version.parse("5.1"):
                    mia_home_config = yaml.load(stream,
                                                Loader=yaml.FullLoader)
                else:
                    mia_home_config = yaml.load(stream)

            mia_home_config["dev_mode"] = False

            with open(dot_mia_config, 'w', encoding='utf8') as configfile:
                yaml.dump(mia_home_config, configfile,
                          default_flow_style=False,
                          allow_unicode=True)

            _verify_miaConfig()

        except Exception as e:  # the configuration.yml file does not exist
            # or has not been correctly read ...
            print('\nA problem has been detected when opening'
                  ' the ~/.populse_mia/configuration.yml file'
                  ' or with the parameters returned from this file: ', e)
            mia_home_config = dict()
            mia_home_config["dev_mode"] = False

            # open popup, user choose the path to .populse_mia/populse_mia
            app = QApplication(sys.argv)
            msg = QDialog()
            msg.setWindowTitle("populse_mia - mia path selection")
            vbox_layout = QVBoxLayout()
            hbox_layout = QHBoxLayout()
            file_label = QLabel("Please select the MIA path (directory with\n "
                                "the processes, properties & resources "
                                "directories): ")
            msg.file_line_edit = QLineEdit()
            msg.file_line_edit.setFixedWidth(400)
            file_button = QPushButton("Browse")
            file_button.clicked.connect(partial(_browse_mia_path, msg))
            vbox_layout.addWidget(file_label)
            hbox_layout.addWidget(msg.file_line_edit)
            hbox_layout.addWidget(file_button)
            vbox_layout.addLayout(hbox_layout)
            hbox_layout = QHBoxLayout()
            msg.ok_button = QPushButton("Ok")
            msg.ok_button.clicked.connect(partial(_verify_miaConfig, msg))
            hbox_layout.addWidget(msg.ok_button)
            vbox_layout.addLayout(hbox_layout)
            msg.setLayout(vbox_layout)
            msg.exec()
            del app

    global pypath

    if DEV_MODE and pypath:
        config = Config()
        config.get_capsul_engine()
        c = config.get_capsul_config()
        pc = c.setdefault('engine', {}).setdefault(
            'global', {}).setdefault('capsul.engine.module.python', {})
        pc['executable'] = sys.executable

        if 'path' in pc:
            matches=[os.path.join('populse_mia', 'python'),
                     'capsul',
                     os.path.join('populse_db', 'python'),
                     os.path.join('mia_processes', 'python'),
                     os.path.join('soma-base', 'python'),
                     os.path.join('soma-workflow', 'python'),
                     os.path.join('populse_mia', 'processes')]

            for i in pc['path']:

               if i not in pypath and not any(x in i for x in matches):
                    pypath.append(i)

        pc['path'] = pypath
        print('\nChanged python conf:', pc)
        config.update_capsul_config()
        config.saveConfig()

    verify_processes()
    check_python_version()
    launch_mia()

    # set the dev_mode to False when exiting mia,
    # if ~/.populse_mia/configuration.yml file exists
    if os.path.isfile(dot_mia_config):

        with open(dot_mia_config, 'r') as stream:

            if version.parse(yaml.__version__) > version.parse("5.1"):
                mia_home_config = yaml.load(stream,
                                            Loader=yaml.FullLoader)
            else:
                mia_home_config = yaml.load(stream)

        mia_home_config["dev_mode"] = False

        with open(dot_mia_config, 'w', encoding='utf8') as configfile:
            yaml.dump(mia_home_config, configfile, default_flow_style=False,
                      allow_unicode=True)


def verify_processes():
    """Install or update to the last version available on the station, of the \
       nipype and the mia_processes processes libraries.

    By default, mia provides two process libraries in the pipeline library
    (available in Pipeline Manager tab). The nipype, given as it is because
    it is developed by another team (https://github.com/nipy/nipype), and
    mia_processes which is developed under the umbrella of populse
    (https://github.com/populse/mia_processes). When installing mia in
    user mode, these two libraries are automatically installed on the
    station. The idea is to use the versioning available with pypi
    (https://pypi.org/). Thus, it is sufficient for the user to change the
    version of the library installed on the station (pip install...) to
    also change the version available in mia. Indeed, when starting mia, the
    verify_processes function will install or update nipype and
    mia_processes libraries in the pipeline library. Currently it is
    mandatory to have nipype and may_processes installed in the station.
    All these informations, as well as the installed versions and package
    paths are saved in the  mia_path/properties/process_config.yml file.
    When an upgrade or downgrade is performed for a package, the last
    configuration used by the user is kept (if a pipeline was visible, it
    remains so and vice versa). However, if a new pipeline is available in
    the new version it is automatically marked as visible in the library.

    :Contains:
        :Private function:
            - *_deepCompDic()*

               Try to keep the previous configuration existing before the
               update of the packages.

               Recursive comparison of the old_dic and new _dic dictionary. If
               all keys are recursively identical, the final value at the end
               of the whole tree in old_dic is kept in the new _dic. To sum
               up, this function is used to keep up the user display
               preferences in the processes library of the Pipeline Manager
               Editor.

               **param old_dic**: the dic representation of the previous
                 package configuration

               **param new_dic**: the dic representation of the new package \
                  configuration

               :returns: True if the current level is a pipeline that existed
                   in the old configuration, False if the
                   package/subpackage/pipeline did not exist

    """

    def _deepCompDic(old_dic, new_dic):
        if isinstance(old_dic, str):
            return True

        for key in old_dic:
            if key not in new_dic:
                pass

            # keep the same configuration for the pipeline in new and old dic
            elif _deepCompDic(old_dic[str(key)], new_dic[str(key)]):
                new_dic[str(key)] = old_dic[str(key)]

    proc_content = False
    nipypeVer = False
    miaProcVer = False
    pack2install = []
    # pack2install: a list containing the package (nipype and/or
    #               mia_processes) to install
    config = Config()
    proc_config = os.path.join(config.get_mia_path(), 'properties',
                               'process_config.yml')
    # check if nipype and mia_processes are available on the station
    # if not available inform the user to install them
    print('\nChecking the installed versions of nipype and mia_processes ...')
    pkg_error = []

    try:
        __import__('nipype')
        nipypeVer = sys.modules['nipype'].__version__

    except (ImportError, AttributeError) as e:
        pkg_error.append('nipype')
        print('\n' + '*' * 37)
        print('MIA warning {0}: {1}'.format(e.__class__, e))
        print('*' * 37 + '\n')

    try:
        __import__('mia_processes')
        miaProcVer = sys.modules['mia_processes'].__version__

    except (ImportError, AttributeError) as e:
        pkg_error.append('mia_processes')
        print('\n' + '*' * 37)
        print('MIA warning {0}: {1}'.format(e.__class__, e))
        print('*' * 37 + '\n')

    from capsul import info as capsul_info
    capsulVer = capsul_info.__version__

    if len(pkg_error) > 0:
        app = QApplication(sys.argv)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("populse_mia -  warning: ImportError!")

        if len(pkg_error) == 1:
            msg.setText("{0} package not found !\nPlease install "
                        "the package and "
                        "start again mia ...".format(pkg_error[0]))
        else:
            msg.setText("{0} and {1} packages not found !\n"
                        "Please install the packages and start again mia "
                        "...".format(pkg_error[0], pkg_error[1]))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(msg.close)
        msg.exec()
        del app
        sys.exit(1)

    if os.path.isfile(proc_config):

        with open(proc_config, 'r') as stream:

            if version.parse(yaml.__version__) > version.parse("5.1"):
                proc_content = yaml.load(stream,
                                         Loader=yaml.FullLoader)
            else:
                proc_content = yaml.load(stream)

    if (isinstance(proc_content, dict)) and ('Packages' in proc_content):
        othPckg = [f for f in proc_content['Packages']
                   if f not in ['mia_processes', 'nipype', 'capsul']]

    if 'othPckg' in dir():
        # othPckg: a list containing all packages, other than nipype and
        # mia_processes, used during the previous launch of mia.

        for pckg in othPckg:

            try:
                __import__(pckg)

            except ImportError as e:
                # try to update the sys.path for the processes/ directory
                # currently used

                if (not (os.path.relpath(os.path.join(config.get_mia_path(),
                                                      'processes')) in
                         sys.path)) and (not (os.path.abspath(os.path.join(
                    config.get_mia_path(), 'processes')) in sys.path)):
                    sys.path.append(os.path.abspath(os.path.join(
                        config.get_mia_path(), 'processes')))

                    try:
                        __import__(pckg)

                        # update the Paths parameter (processes/ directory
                        # currently used) saved later in the
                        # mia_path/properties/process_config.yml file
                        if (('Paths' in proc_content)
                                and (isinstance(proc_content['Paths'], list))):

                            if ((not os.path.relpath(os.path.join(
                                    config.get_mia_path(), 'processes')) in
                                     proc_content['Paths'])
                                    and (
                                            not os.path.abspath(os.path.join(
                                                config.get_mia_path(),
                                                'processes')) in
                                                proc_content['Paths'])):
                                proc_content['Paths'].append(os.path.abspath(
                                    os.path.join(
                                        config.get_mia_path(), 'processes')))

                        else:
                            proc_content['Paths'] = [os.path.abspath(
                                os.path.join(config.get_mia_path(),
                                             'processes'))]

                        with open(proc_config, 'w', encoding='utf8') as stream:
                            yaml.dump(proc_content, stream,
                                      default_flow_style=False,
                                      allow_unicode=True)

                        # finally the processes/ directory currently used is
                        # removed from the sys.path because this directory is
                        # now added to the Paths parameter in the
                        # mia_path/properties/process_config.yml file
                        sys.path.remove(os.path.abspath(os.path.join(
                            config.get_mia_path(), 'processes')))

                    # if an exception is raised, ask to the user to remove the
                    # package from the pipeline library or reload it
                    except ImportError as e:
                        print('\n{0}'.format(e))
                        app = QApplication(sys.argv)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setWindowTitle("populse_mia - warning: {0}"
                                           .format(e))
                        msg.setText(("At least, {0} has not been found in {1}."
                                     "\nTo prevent mia crash when using it, "
                                     "please remove (see File > Package "
                                     "library manager) or load again (see More"
                                     " > Install processes) the corresponding "
                                     "process library.").format(
                            e.msg.split()[-1], os.path.abspath(os.path.join(
                                config.get_mia_path(), 'processes', pckg))))
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.buttonClicked.connect(msg.close)
                        msg.exec()
                        del app
                        sys.path.remove(os.path.abspath(os.path.join(
                            config.get_mia_path(), 'processes')))

                # the processes/ directory being already in the sys.path, the
                # package is certainly not properly installed in the processes/
                # directory
                else:
                    print("No module named '{0}'".format(pckg))
                    app = QApplication(sys.argv)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("populse_mia - warning: {0}".format(e))
                    msg.setText(("At least, {0} has not been found in {1}."
                                 "\nTo prevent mia crash when using it, "
                                 "please remove (see File > Package "
                                 "library manager) or load again (see More"
                                 " > Install processes) the corresponding "
                                 "process library.").format(
                        e.msg.split()[-1], os.path.abspath(os.path.join(
                            config.get_mia_path(), 'processes'))))
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.buttonClicked.connect(msg.close)
                    msg.exec()
                    del app

    # the file mia_path/properties/process_config.yml is corrupted or
    # no pipeline processes was available during the previous use of mia or
    # their version is not known
    if ((not isinstance(proc_content, dict)) or
            ((isinstance(proc_content, dict))
             and ('Packages' not in proc_content)) or
            ((isinstance(proc_content, dict))
             and ('Versions' not in proc_content))):
        pack2install = ['nipype.interfaces', 'mia_processes', 'capsul']
        old_nipypeVer = None
        old_miaProcVer = None

    else:

        # during the previous use of mia, nipype was not available or its
        # version was not known or its version was different from the one
        # currently available on the station
        if ((isinstance(proc_content, dict)) and
                ('Packages' in proc_content) and
                ('nipype' not in proc_content['Packages'])):
            old_nipypeVer = None
            pack2install.append('nipype.interfaces')

            if ((isinstance(proc_content, dict)) and
                    ('Versions' in proc_content) and
                    ('nipype' in proc_content['Versions'])):
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the nipype processes "
                      "library again in mia ...")

        else:

            if (((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('nipype' not in proc_content['Versions'])) or
                    ((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('nipype' in proc_content['Versions'])
                    and (proc_content['Versions']['nipype'] is None))):
                old_nipypeVer = None
                pack2install.append('nipype.interfaces')
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the nipype processes "
                      "library again in mia ...")

            elif ((isinstance(proc_content, dict)) and
                    ('Versions' in proc_content) and
                    ('nipype' in proc_content['Versions']) and
                    (proc_content['Versions']['nipype'] != nipypeVer)):
                old_nipypeVer = proc_content['Versions']['nipype']
                pack2install.append('nipype.interfaces')

        # during the previous use of mia, mia_processes was not available or
        # its version was not known or its version was different from the one
        # currently available on the station
        if ((isinstance(proc_content, dict)) and
            ('Packages' in proc_content) and
            ('mia_processes' not in proc_content['Packages'])):
            old_miaProcVer = None
            pack2install.append('mia_processes')

            if ((isinstance(proc_content, dict)) and
                ('Versions' in proc_content) and
                ('mia_processes' in proc_content['Versions'])):
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the mia_processes "
                      "processes library again in mia ...")

        else:

            if (((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('mia_processes' not in proc_content['Versions'])) or
                    ((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('mia_processes' in proc_content['Versions'])
                    and (proc_content['Versions']['mia_processes'] is None))):
                old_miaProcVer = None
                pack2install.append('mia_processes')
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the mia_processes "
                      "processes library again in mia ...")

            elif ((isinstance(proc_content, dict)) and
                  ('Versions' in proc_content) and
                  ('mia_processes' in proc_content['Versions']) and
                  (proc_content['Versions']['mia_processes'] != miaProcVer)):
                 old_miaProcVer = proc_content['Versions']['mia_processes']
                 pack2install.append('mia_processes')

        # during the previous use of mia, capsul was not available or
        # its version was not known or its version was different from the one
        # currently available on the station
        if ((isinstance(proc_content, dict)) and
            ('Packages' in proc_content) and
            ('capsul' not in proc_content['Packages'])):
            old_capsulVer = None
            pack2install.append('capsul.pipeline.custom_nodes')

            if ((isinstance(proc_content, dict)) and
                ('Versions' in proc_content) and
                ('capsul' in proc_content['Versions'])):
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the capsul "
                      "processes library again in mia ...")

        else:

            if (((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('capsul' not in proc_content['Versions'])) or
                    ((isinstance(proc_content, dict))
                    and ('Versions' in proc_content)
                    and ('capsul' in proc_content['Versions'])
                    and (proc_content['Versions']['capsul'] is None))):
                old_capsulVer = None
                pack2install.append('capsul.pipeline.custom_nodes')
                print("\nThe process_config.yml file seems to be corrupted! "
                      "Let's try to fix it by installing the capsul "
                      "processes library again in mia ...")

            elif ((isinstance(proc_content, dict)) and
                  ('Versions' in proc_content) and
                  ('capsul' in proc_content['Versions']) and
                  (proc_content['Versions']['capsul'] != capsulVer)):
                 old_capsulVer = proc_content['Versions']['capsul']
                 pack2install.append('capsul.pipeline.custom_nodes')

    final_pckgs = dict()          # final_pckgs: the final dic of dic with the
    final_pckgs["Packages"] = {}  # informations about the installed packages,
    final_pckgs["Versions"] = {}  # their versions, and the path to access them

    for pckg in pack2install:
        package = PackagesInstall()

        if 'nipype' in pckg:  # Save the packages version
            final_pckgs["Versions"]["nipype"] = nipypeVer

            if old_nipypeVer is None:
                print('\n** Installation in mia of the {0} processes library, '
                  '{1} version ...'.format(pckg, nipypeVer))

            else:
                print('\n** Upgrading of the {0} processes library, '
                  'from {1} to {2} version ...'.format(pckg,
                                                       old_nipypeVer,
                                                       nipypeVer))

        if 'mia_processes' in pckg:
            final_pckgs["Versions"]["mia_processes"] = miaProcVer

            if old_miaProcVer is None:
                 print('\n** Installation in mia of the {0} processes library, '
                  '{1} version ...'.format(pckg, miaProcVer ))

            else:
                print('\n** Upgrading of the {0} processes library, '
                  'from {1} to {2} version ...'.format(pckg,
                                                       old_miaProcVer,
                                                       miaProcVer))

        if 'capsul' in pckg:
            final_pckgs["Versions"]["capsul"] = capsulVer

            if old_capsulVer is None:
                 print('\n** Installation in mia of the {0} processes library, '
                  '{1} version ...'.format(pckg, capsulVer ))

            else:
                print('\n** Upgrading of the {0} processes library, '
                  'from {1} to {2} version ...'.format(pckg,
                                                       old_capsulVer,
                                                       capsulVer))

        print('\nExploring {0} ...'.format(pckg))
        pckg_dic = package.add_package(pckg)
        # pckg_dic: a dic of dic representation of a package and its
        #           subpackages/modules
        #           Ex. {package: {subpackage: {pipeline:'process_enabled'}}}


        for item in pckg_dic:
            final_pckgs["Packages"][item] = pckg_dic[item]

    if pack2install:

        if not any("nipype" in s for s in pack2install):
            print('\n** The nipype processes library in mia is '
                  'already using the current installed version ({0}) '
                  'for this station\n'.format(nipypeVer))

        elif not any("mia_processes" in s for s in pack2install):
            print('\n** The mia_processes library in mia is '
                  'already using the current installed version ({0}) '
                  'for this station\n'.format(miaProcVer))

        elif not any("capsul" in s for s in pack2install):
            print('\n** The capsul library in mia is '
                  'already using the current installed version ({0}) '
                  'for this station\n'.format(capsulVer))

        if (isinstance(proc_content, dict)) and ('Paths' in proc_content):

            for item in proc_content['Paths']:  # Save the path to the packages
                final_pckgs["Paths"] = proc_content['Paths']

        if (isinstance(proc_content, dict)) and ('Versions' in proc_content):
            for item in proc_content['Versions']:

                if item not in final_pckgs['Versions']:
                    final_pckgs['Versions'][item] = proc_content[
                        'Versions'][item]

        # try to keep the previous configuration before the update
        # of the packages
        if (isinstance(proc_content, dict)) and ('Packages' in proc_content):
            _deepCompDic(proc_content['Packages'], final_pckgs['Packages'])
            for item in proc_content['Packages']:
                if item not in final_pckgs['Packages']:
                    final_pckgs['Packages'][item] = proc_content[
                        'Packages'][item]

        with open(proc_config, 'w', encoding='utf8') as stream:
            yaml.dump(final_pckgs, stream, default_flow_style=False,
                      allow_unicode=True)

    else:
        print('\n** mia is already using the current installed version of '
              'nipype, mia_processes and capsul for this station ({0}, {1} '
              'and {2}, respectively)\n'.format(nipypeVer, miaProcVer,
                                                capsulVer))


if __name__ == '__main__':
    # this will only be executed when this module is run directly
    main()
