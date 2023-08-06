# -*- coding: utf8 -*-
#============================================
#   TreeWalker
#   ~~~~~~~~~~~
#
#   Walk a directory tree processing files
#============================================

import os

class TreeWalker(object):

    def __init__(self, root_path, ext = '', callback=None):
        apath = os.path.abspath(root_path)
        self.root = apath
        self.callback = callback
        self.extension = ext

    def set_extension(self, extension):
        self.extension = extension

    def set_callback(selfself, callback):
        self.callback = callback

    def run(self):
        for dirpath, dirnames, filenames in os.walk(self.root):
                for f in filenames:
                    # run the callback
                    path = os.path.abspath(os.path.join(dirpath, f))
                    if path.endswith(self.extension):
                        if not self.callback is None:
                            self.callback(path)

    def get_file_list(self):
        flist = []
        for dirpath, dirnames, filenames in os.walk(self.root):
            for f in filenames:
                # run the callback
                path = os.path.abspath(os.path.join(dirpath, f))
                if path.endswith(self.extension):
                        flist.append(path)
        return flist

    def get_leaf_file_list(self):
        llist = []
        for dirpath, dirnames, filenames in os.walk(self.root):
            if len(dirnames) != 0: continue
            for f in filenames:
                path = os.path.abspath(os.path.join(dirpath, f))
                if path.endswith(self.extension):
                    llist.append(path)
        return llist

def print_tree(filename):
    print("callback : ", filename)


if __name__ == "__main__":
    PROJECT = "../scad/math-magik-lpp"
    project = os.path.abspath(PROJECT)
    print(project)
    tw = TreeWalker(PROJECT,'scad', print_tree)
    tw.run()
    #flist = tw.get_file_list()
    #print(flist)
    #tw.set_extension('.stl')
    slist = tw.get_leaf_file_list()
    print(len(slist))
    for s in slist:
        print(s)
