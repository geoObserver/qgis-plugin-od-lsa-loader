from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.utils import *

class OD_LSA_Loader:
    def __init__(self, iface):
        self.iface = iface
        
    def initGui(self):
        self.startButtonT1 = QAction('—————————————————————————', self.iface.mainWindow())
        self.startButtonT2 = QAction('—————————————————————————', self.iface.mainWindow())
        self.startButtonT3 = QAction('—————————————————————————', self.iface.mainWindow())

        self.startButton10 = QAction('LSA: ALKIS Flurstücke (WMS)', self.iface.mainWindow())
        self.startButton11 = QAction('LSA: ALKIS Gebäude (WMS)', self.iface.mainWindow())
        self.startButton12 = QAction('LSA: ALKIS Tatsächliche Nutzung (WMS)', self.iface.mainWindow())
        self.startButton13 = QAction('LSA: ALKIS Flurstücke (WFS)', self.iface.mainWindow())
        self.startButton14 = QAction('LSA: ALKIS Gebäude (WFS)', self.iface.mainWindow())
        self.startButton50 = QAction('LSA: Digitale Orthophotos - DOP20 (WMS)', self.iface.mainWindow())
        self.startButton51 = QAction('LSA: Digitale Orthophotos - DOP100 (WMS)', self.iface.mainWindow())
        self.startButton90 = QAction('OSM-Hintergrundkarte  (XYZ)', self.iface.mainWindow())
        self.startButton91 = QAction('basemap.de-Hintergrundkarte grau (WMS)', self.iface.mainWindow())
        self.startButton92 = QAction('basemap.de-Hintergrundkarte farbig (WMS)', self.iface.mainWindow())

        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton10)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton11)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton12)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButtonT1) # ------------
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton13)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton14)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButtonT2) # ------------
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton50)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton51)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButtonT3) # ------------
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton90)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton91)
        self.iface.addPluginToMenu('OD_LSA_Loader', self.startButton92)

        self.startButton10.triggered.connect(self.addWMS10)
        self.startButton11.triggered.connect(self.addWMS11)
        self.startButton12.triggered.connect(self.addWMS12)
        self.startButton13.triggered.connect(self.addWFS13)
        self.startButton14.triggered.connect(self.addWFS14)
        self.startButton50.triggered.connect(self.addWMS50)
        self.startButton51.triggered.connect(self.addWMS51)
        self.startButton90.triggered.connect(self.addWMS90)
        self.startButton91.triggered.connect(self.addWMS91)
        self.startButton92.triggered.connect(self.addWMS92)
            
    def unload(self):
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButtonT1)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButtonT2)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton10)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton11)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton12)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton13)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton14)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton50)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton51)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton90)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton91)
        self.iface.removePluginMenu('OD_LSA_Loader', self.startButton92)
           
    def addWMS90(self):
        uri90 = '&type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0'
        lyr90 = QgsRasterLayer(uri90, 'OSM Hintergrundkarte (XYZ)', 'wms')
        QgsProject.instance().addMapLayer(lyr90)
                        
    def addWMS91(self):
        uri91 = 'crs=EPSG:3857&dpiMode=7&format=image/png&layers=de_basemapde_web_raster_grau&styles&tilePixelRatio=0&url=https://sgx.geodatenzentrum.de/wms_basemapde?REQUEST%3DGetCapabilities%26Version%3D1.3.0'
        lyr91 = QgsRasterLayer(uri91, 'basemap.de grau (WMS)', 'wms')
        QgsProject.instance().addMapLayer(lyr91)
        
    def addWMS92(self):
        uri92 = 'crs=EPSG:3857&dpiMode=7&format=image/png&layers=de_basemapde_web_raster_farbe&styles&tilePixelRatio=0&url=https://sgx.geodatenzentrum.de/wms_basemapde?REQUEST%3DGetCapabilities%26Version%3D1.3.0'
        lyr92 = QgsRasterLayer(uri92, 'basemap.de farbig (WMS)', 'wms')
        QgsProject.instance().addMapLayer(lyr92)
        
    def addWMS50(self):
        uri50 = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dop20_2&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DOP_WMS_OpenData/guest'
        lyr50 = QgsRasterLayer(uri50, 'LSA: DOP20 (WMS)', 'wms')
        QgsProject.instance().addMapLayer(lyr50) 
          
    def addWMS51(self):
        uri51 = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dop100_unbesch&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DOP_WMS_OpenData/guest'
        lyr51 = QgsRasterLayer(uri51, 'LSA: DOP100 (WMS)', 'wms')
        QgsProject.instance().addMapLayer(lyr51) 
          
    def addWMS10(self):
        uri10 = 'crs=EPSG:25832&dpiMode=5&format=image/png&layers=adv_alkis_flurstuecke&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr10 = QgsRasterLayer(uri10, 'LSA: ALKIS Flurstücke (WMS)', 'wms')
        QgsProject.instance().addMapLayer(lyr10)
        
    def addWMS11(self):
        uri11 = 'crs=EPSG:25832&dpiMode=5&format=image/png&layers=adv_alkis_gebaeude&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr11 = QgsRasterLayer(uri11, 'LSA: ALKIS Gebäude (WMS)', 'wms')
        lyr11.renderer().setOpacity(0.75)
        QgsProject.instance().addMapLayer(lyr11)
        
    def addWMS12(self):
        myroot = QgsProject.instance().layerTreeRoot()
        mygroup = myroot.insertGroup(0, 'LSA: ALKIS Tats. Nutzung (WMS)')
        
        uri12a = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_gewaesser&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr12a = QgsRasterLayer(uri12a, 'Gewässer', 'wms')
        lyr12a.renderer().setOpacity(0.75)
        QgsProject.instance().addMapLayer(lyr12a, False)
        mygroup.addLayer(lyr12a) 
        
        uri12b = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_siedlung&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr12b = QgsRasterLayer(uri12b, 'Siedlung', 'wms')
        lyr12b.renderer().setOpacity(0.75)
        #QgsProject.instance().addMapLayer(lyr12b)
        QgsProject.instance().addMapLayer(lyr12b, False)
        mygroup.addLayer(lyr12b) 
        
        uri12c = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_vegetation&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr12c = QgsRasterLayer(uri12c, 'Vegetation', 'wms')
        lyr12c.renderer().setOpacity(0.75)
        #QgsProject.instance().addMapLayer(lyr12c)
        QgsProject.instance().addMapLayer(lyr12c, False)
        mygroup.addLayer(lyr12c) 
        
        uri12d = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_verkehr&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        lyr12d = QgsRasterLayer(uri12d, 'Verkehr', 'wms')
        lyr12d.renderer().setOpacity(0.75)
        #QgsProject.instance().addMapLayer(lyr12d)
        QgsProject.instance().addMapLayer(lyr12d, False)
        mygroup.addLayer(lyr12d)
        
    def addWFS13(self):
        uri = 'https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WFS_OpenData/guest?&service=WFS&BBOX=1332412,6708967,1333423,6709355&restrictToRequestBBOX=1&VERSION=auto&typename=ave:Flurstueck&srsname=EPSG:25832&preferCoordinatesForWfsT11=false&pagingEnabled=true'
        lyr13 = QgsVectorLayer(uri, "LSA: ALKIS Flurstücke (WFS)" , 'WFS')
        lyr13.setOpacity(0.75) 
        lyr13.setMinimumScale(25000.0)
        lyr13.setMaximumScale(1.0)
        # Farbe ändern
        lyr13.renderer().symbol().setColor(QColor("transparent"))
        lyr13.renderer().symbol().symbolLayer(0).setStrokeColor(QColor("black"))
        lyr13.renderer().symbol().symbolLayer(0).setStrokeWidth(0.2)
        lyr13.triggerRepaint() #braucht es nur wenn schon geladen
        # Legende updaten
        iface.layerTreeView().refreshLayerSymbology(lyr13.id())
        lyr13.setScaleBasedVisibility(1)
        QgsProject.instance().addMapLayer(lyr13)

    def addWFS14(self):
        uri = 'https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WFS_OpenData/guest?&service=WFS&BBOX=1332412,6708967,1333423,6709355&restrictToRequestBBOX=1&VERSION=auto&typename=ave:GebaeudeBauwerk&srsname=EPSG:25832&preferCoordinatesForWfsT11=false&pagingEnabled=true'
        lyr14 = QgsVectorLayer(uri, "LSA: ALKIS Gebäude (WFS)" , 'WFS')
        # Opazität ändern
        lyr14.setOpacity(0.75)
        # Massstabsklassen/Sichtbarkeit ändern
        lyr14.setMinimumScale(25000.0)
        lyr14.setMaximumScale(1.0)
        # Farbe ändern
        lyr14.renderer().symbol().setColor(QColor(220,220,220))
        lyr14.renderer().symbol().symbolLayer(0).setStrokeColor(QColor("black"))
        lyr14.renderer().symbol().symbolLayer(0).setStrokeWidth(0.1)
        lyr14.triggerRepaint() #braucht es nur wenn schon geladen
        # Legende updaten
        iface.layerTreeView().refreshLayerSymbology(lyr14.id())
        lyr14.setScaleBasedVisibility(1)
        QgsProject.instance().addMapLayer(lyr14)
      
        