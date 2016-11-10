from setuptools import setup, find_packages
import os
import sys

if 'help' in sys.argv[:]:
    print("MANUAL:")
    print("=======")
    print("To build interfaces")
    print("> python setup.py pyuic")
    print("To build icons listing")
    print("> python setup.py pyrcc")
    sys.exit(0)

if 'pyuic' in sys.argv[:]:
    indir = 'designer'
    outdir = 'mygui/interfaces'
    files = os.listdir(indir)
    files = [os.path.join('designer', item) for item in files]
    files = [item for item in files if item.endswith('.ui')]

    done = 0
    for inname in files:
        outname = inname.replace('.ui', '.py')
        outname = outname.replace(indir, outdir)
        if os.path.exists(outname):
            if os.stat(inname).st_mtime < os.stat(outname).st_mtime:
                continue
        print("Converting '%s' to '%s'" % (inname, outname))
        command = "pyuic4 %s -o %s"  % (inname, outname)
        os.system(command)
        done += 1
    if not done:
        print("Did not convert any '.ui' files")
    sys.exit(0)

if 'pyrcc' in sys.argv[:]:
    infile = './icons/icons.qrc'
    assert os.path.isfile(infile)
    outfile = './mygui/interfaces/icons_rc.py'
    print("Converting icons_rc file:")
    command = "pyrcc4  %s -o %s" % (infile, outfile)
    print("> %s" %command)
    os.system(command)
    sys.exit(0)

setup(name="iBeatles",
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description = "Description here",
      author = "Name of author here",
      author_email = "email of author here",
      url = "http://github.com/JeanBilheux/PyQtGuiBase",
      long_description = """Should have a longer description""",
      license = "The MIT License (MIT)",
      scripts=["scripts/myGui"],
      packages=find_packages(),
      package_dir={},
      install_requires=['numpy','matplotlib'],
      setup_requires=[],
)
