USE_VIRTUAL_ENV="TRUE"
if [ $USE_VIRTUAL_ENV = "TRUE" ]; then
# create a virtualenv if it doesn't already exist
        if [ ! -f ./gui_env/bin/activate ]; then
            pip install --user virtualenv
            virtualenv -p "/usr/bin/python2" --system-site-packages gui_env
            echo "source $(pwd)/gui_env/bin/activate" >> source_gui_env.bash
            source gui_env/bin/activate
            pip install pyside2
        fi
fi

