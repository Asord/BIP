import bpy
from Managers.XMLParser import debug
#from Interface.Props import PropNumberSlide


class Slides(object):

    def __init__(self, gestionSlide, slidePos):
        self.gestionSlide = gestionSlide
        """bpy.ops.object.camera_add(location = (slidePos*20,5,0), rotation = (90,0,0))
        bpy.context.active_object.name = 'cam'
        self.camera = bpy.data.objects["cam"]"""
        self.cameraPos = [slidePos*20,5,0]
        self.transitionDone = False
        self.actionDone = False
        self.listObjects = []

    def addObject(self, obj):
        self.listObjects.append(obj)

    def removeObject(self, obj):
        for i in range(0, len(self.listObjects) - 1):
            if self.listObjects[i] == obj:
                del self.listObjects[i]

    def _getid(self):
        return self.gestionSlide.listSlides.index(self)

    def startTransition(self):

        """TODO"""

        self.transitionDone = True

    def startAction(self):

        """TODO"""

        self.actionDone = True

    def next(self):
        if self.transitionDone and self.actionDone:
            self.gestionSlide.setActiveSlide(self._getid()+1)
            bpy.context.scene.camera = self.gestionSlide.listSlides[self._getid()+1].camera

    def __del__(self):
        del self


class GestionSlides(object):

    class __GestionSlides(object):

        def __init__(self):

            self.nbSlides = 0
            self.posActiveSlide = -1
            self.listSlides = []
            self.camera = None
            self.isCameraView = False

        def addSlide(self):
            """if self.nbSlides == 0 or self.nbSlides == 1:
                self.listSlides.append(Slides(self, self.nbSlides))
            else:
                if self.posActiveSlide + 1 == self.nbSlides:
                    self.listSlides.append(Slides(self, self.nbSlides))
                else:
                    self.listSlides.insert(self.posActiveSlide + 1, Slides(self, self.posActiveSlide + 1))
                    for i in range(self.posActiveSlide + 2, self.nbSlides + 1):
                        self.listSlides[i].camera.location.x += 20
                        for j in range(0, len(self.listSlides[i].listObjects) - 1):
                            self.listSlides[i].listObjects[j].location.x += 20"""

            if self.nbSlides == 0:
                self.listSlides.append(Slides(self,0))
                bpy.ops.object.camera_add(location=self.listSlides[0].cameraPos, rotation= (1.5708, 0, 0)) #Angle euler
                bpy.context.active_object.name = 'cam'
                self.camera = bpy.data.objects["cam"]

            else:
                if self.posActiveSlide + 1 == self.nbSlides:
                    self.listSlides.append(Slides(self, self.nbSlides))
                    bpy.ops.object.select_all(action='DESELECT')
                    self.camera.select = True
                    self.camera.location = self.listSlides[self.nbSlides].cameraPos

                else:
                    self.listSlides.insert(self.posActiveSlide + 1, Slides(self, self.posActiveSlide + 1))
                    bpy.ops.object.select_all(action='DESELECT')
                    self.camera.select = True
                    self.camera.location = self.listSlides[self.posActiveSlide + 2].cameraPos
                    for i in range(self.posActiveSlide + 2, self.nbSlides + 1):
                        debug('Pos', self.listSlides[i].cameraPos)
                        self.listSlides[i].cameraPos[0] += 20
                        for j in range(0, len(self.listSlides[i].listObjects) - 1):
                            self.listSlides[i].listObjects[j].location.x += 20

            bpy.context.scene.prop_nb_slides['Active_Slide'] = self.posActiveSlide + 2
            self.posActiveSlide += 1

            self.addNbSlide()


        def getNbSlides(self):
            return self.nbSlides

        def addNbSlide(self):
            self.nbSlides += 1

        def subNbSlide(self):
            self.nbSlides -= 1

        def getActiveSlide(self):
            return self.posActiveSlide

        def setActiveSlide(self, value):
            if value <= len(self.listSlides):
                self.posActiveSlide = value - 1
                self.camera.location = self.listSlides[self.posActiveSlide].cameraPos
                bpy.ops.object.select_all(action='DESELECT')
                self.camera.select = True
                bpy.ops.view3d.snap_cursor_to_active()
                bpy.context.space_data.cursor_location[1] = 30

        def removeSlide(self):
            if self.nbSlides == 1:
                bpy.ops.object.select_all(action='DESELECT')
                self.camera.select = True
                bpy.ops.object.delete()
                del self.listSlides[0]
                bpy.context.scene.prop_nb_slides['Active_Slide'] = 0

            else:
                for i in range(self.posActiveSlide + 1, len(self.listSlides)):
                    self.listSlides[i].cameraPos[0] -= 20
                    for j in range(0, len(self.listSlides[i].listObjects)):
                        self.listSlides[i].listObjects[j].location.x -= 20

                del self.listSlides[self.posActiveSlide]

                bpy.context.scene.prop_nb_slides['Active_Slide'] = self.posActiveSlide
                self.camera.location = self.listSlides[self.posActiveSlide - 1].cameraPos
                bpy.ops.object.select_all(action='DESELECT')
                self.camera.select = True

                if self.isCameraView:
                    bpy.context.space_data.cursor_location[0] -= 20

            self.posActiveSlide -= 1

            self.subNbSlide()


    instance = None

    def __new__(cls):
        if SlidesManager.instance is None:
            SlidesManager.instance = SlidesManager.__GestionSlides()
        return SlidesManager.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
