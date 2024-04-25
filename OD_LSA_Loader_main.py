from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.utils import *

class OD_LSA_Loader:
    version = '0.0.7'
    myPlugin = 'OD_LSA_Loader'
    myPluginV = myPlugin + ' v' + version
    myCritical_1 = u'Fehler beim Laden des Layers '
    myCritical_2 = u', Dienst nicht verfügbar (URL?)'
    myInfo_1 = u'Layer '
    myInfo_2 = u' erfolgreich geladen.'
    
    def __init__(self, iface):
        self.iface = iface
    
    def initGui(self):
        self.startButtonT0 = QAction('◼︎◼︎◼︎ ' + self.myPluginV + ' ◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎', self.iface.mainWindow())
        self.startButtonT1 = QAction('—————————————————————————', self.iface.mainWindow())
        self.startButtonT2 = QAction('—————————————————————————', self.iface.mainWindow())
        self.startButtonT3 = QAction('—————————————————————————', self.iface.mainWindow())
        self.startButtonT4 = QAction('—————————————————————————', self.iface.mainWindow())

        self.startButton10 = QAction('LSA: ALKIS Flurstücke (WMS)', self.iface.mainWindow())
        self.startButton11 = QAction('LSA: ALKIS Gebäude (WMS)', self.iface.mainWindow())
        self.startButton12 = QAction('LSA: ALKIS Tatsächliche Nutzung (WMS)', self.iface.mainWindow())
        self.startButton15 = QAction('LSA: Bodenrichtwerte Bauland (WMS)', self.iface.mainWindow())
        self.startButton13 = QAction('LSA: ALKIS Flurstücke (WFS)', self.iface.mainWindow())
        self.startButton14 = QAction('LSA: ALKIS Gebäude (WFS)', self.iface.mainWindow())
        self.startButton21 = QAction('LSA: Topograf. Karten farbig (WMS)', self.iface.mainWindow())
        self.startButton22 = QAction('LSA: Topograf. Karten grau (WMS)', self.iface.mainWindow())
        self.startButton50 = QAction('LSA: Digitale Orthophotos - DOP20 (WMS)', self.iface.mainWindow())
        self.startButton51 = QAction('LSA: Digitale Orthophotos - DOP100 (WMS)', self.iface.mainWindow())
        self.startButton90 = QAction('OSM-Hintergrundkarte  (XYZ)', self.iface.mainWindow())
        self.startButton91 = QAction('basemap.de-Hintergrundkarte grau (WMS)', self.iface.mainWindow())
        self.startButton92 = QAction('basemap.de-Hintergrundkarte farbig (WMS)', self.iface.mainWindow())
        self.startButton93 = QAction('BONUS! HAL: Digitale Stadtgrundkarte (WMS)', self.iface.mainWindow())

        self.iface.addPluginToMenu(self.myPlugin, self.startButtonT0)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton10)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton11)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton12)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton15)
        self.iface.addPluginToMenu(self.myPlugin, self.startButtonT1) # ------------
        self.iface.addPluginToMenu(self.myPlugin, self.startButton13)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton14)
        self.iface.addPluginToMenu(self.myPlugin, self.startButtonT4) # ------------
        self.iface.addPluginToMenu(self.myPlugin, self.startButton21)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton22)
        self.iface.addPluginToMenu(self.myPlugin, self.startButtonT2) # ------------
        self.iface.addPluginToMenu(self.myPlugin, self.startButton50)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton51)
        self.iface.addPluginToMenu(self.myPlugin, self.startButtonT3) # ------------
        self.iface.addPluginToMenu(self.myPlugin, self.startButton90)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton91)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton92)
        self.iface.addPluginToMenu(self.myPlugin, self.startButton93)

        self.startButton10.triggered.connect(self.addWMS10)
        self.startButton11.triggered.connect(self.addWMS11)
        self.startButton12.triggered.connect(self.addWMS12)
        self.startButton13.triggered.connect(self.addWFS13)
        self.startButton14.triggered.connect(self.addWFS14)
        self.startButton15.triggered.connect(self.addWMS15)
        self.startButton21.triggered.connect(self.addWMS21)
        self.startButton22.triggered.connect(self.addWMS22)
        self.startButton50.triggered.connect(self.addWMS50)
        self.startButton51.triggered.connect(self.addWMS51)
        self.startButton90.triggered.connect(self.addWMS90)
        self.startButton91.triggered.connect(self.addWMS91)
        self.startButton92.triggered.connect(self.addWMS92)
        self.startButton93.triggered.connect(self.addWMS93)
            
    def unload(self):
        self.iface.removePluginMenu(self.myPlugin, self.startButtonT0)
        self.iface.removePluginMenu(self.myPlugin, self.startButtonT1)
        self.iface.removePluginMenu(self.myPlugin, self.startButtonT2)
        self.iface.removePluginMenu(self.myPlugin, self.startButtonT3)
        self.iface.removePluginMenu(self.myPlugin, self.startButton10)
        self.iface.removePluginMenu(self.myPlugin, self.startButton11)
        self.iface.removePluginMenu(self.myPlugin, self.startButton12)
        self.iface.removePluginMenu(self.myPlugin, self.startButton13)
        self.iface.removePluginMenu(self.myPlugin, self.startButton14)
        self.iface.removePluginMenu(self.myPlugin, self.startButton15)
        self.iface.removePluginMenu(self.myPlugin, self.startButton21)
        self.iface.removePluginMenu(self.myPlugin, self.startButton22)
        self.iface.removePluginMenu(self.myPlugin, self.startButton50)
        self.iface.removePluginMenu(self.myPlugin, self.startButton51)
        self.iface.removePluginMenu(self.myPlugin, self.startButton90)
        self.iface.removePluginMenu(self.myPlugin, self.startButton91)
        self.iface.removePluginMenu(self.myPlugin, self.startButton92)
        self.iface.removePluginMenu(self.myPlugin, self.startButton93)
           
    def addWMS90(self):
        uri90 = '&type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0'
        name = 'OSM Hintergrundkarte (XYZ)'
        lyr90 = QgsRasterLayer(uri90, name, 'wms')
        if not lyr90.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            QgsProject.instance().addMapLayer(lyr90)
            iface.messageBar().pushMessage(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)
                        
    def addWMS91(self):
        uri91 = 'crs=EPSG:3857&dpiMode=7&format=image/png&layers=de_basemapde_web_raster_grau&styles&tilePixelRatio=0&url=https://sgx.geodatenzentrum.de/wms_basemapde?REQUEST%3DGetCapabilities%26Version%3D1.3.0'
        name = 'basemap.de grau (WMS)'
        lyr91 = QgsRasterLayer(uri91, name, 'wms')
        if not lyr91.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)
        else:
            QgsProject.instance().addMapLayer(lyr91)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        
            
    def addWMS92(self):
        uri92 = 'crs=EPSG:3857&dpiMode=7&format=image/png&layers=de_basemapde_web_raster_farbe&styles&tilePixelRatio=0&url=https://sgx.geodatenzentrum.de/wms_basemapde?REQUEST%3DGetCapabilities%26Version%3D1.3.0'
        name = 'basemap.de farbig (WMS)'
        lyr92 = QgsRasterLayer(uri92, name, 'wms')
        if not lyr92.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)
        else:
            QgsProject.instance().addMapLayer(lyr92)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        
                
    def addWMS50(self):
        uri50 = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dop20_2&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DOP_WMS_OpenData/guest'
        name = 'LSA: DOP20 (WMS)'
        lyr50 = QgsRasterLayer(uri50, name, 'wms')
        if not lyr50.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            QgsProject.instance().addMapLayer(lyr50) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        
          
    def addWMS51(self):
        uri51 = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dop100_unbesch&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DOP_WMS_OpenData/guest'
        name = 'LSA: DOP100 (WMS)'
        lyr51 = QgsRasterLayer(uri51, name, 'wms')
        if not lyr51.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            QgsProject.instance().addMapLayer(lyr51)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

    def addWMS10(self):
        uri10 = 'crs=EPSG:25832&dpiMode=5&format=image/png&layers=adv_alkis_flurstuecke&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'LSA: ALKIS Flurstücke (WMS)'
        lyr10 = QgsRasterLayer(uri10, name, 'wms')
        if not lyr10.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            #lyr10.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr10)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2) 
        
    def addWMS11(self):
        uri11 = 'crs=EPSG:25832&dpiMode=5&format=image/png&layers=adv_alkis_gebaeude&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'LSA: ALKIS Gebäude (WMS)'
        lyr11 = QgsRasterLayer(uri11, name, 'wms')
        if not lyr11.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr11.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr11)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

    def addWMS12(self):
        myroot = QgsProject.instance().layerTreeRoot()
        mygroup = myroot.insertGroup(0, 'LSA: ALKIS Tats. Nutzung (WMS)')
        
        uri12a = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_gewaesser&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'Gewässer'
        lyr12a = QgsRasterLayer(uri12a, name, 'wms')
        if not lyr12a.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr12a.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr12a, False)
            mygroup.addLayer(lyr12a)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)  
        
        uri12b = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_siedlung&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'Siedlung'
        lyr12b = QgsRasterLayer(uri12b, name, 'wms')
        if not lyr12b.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr12b.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr12b, False)
            mygroup.addLayer(lyr12b)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)  
       
        uri12c = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_vegetation&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'Vegetation'
        lyr12c = QgsRasterLayer(uri12c, name, 'wms')
        if not lyr12c.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr12c.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr12c, False)
            mygroup.addLayer(lyr12c) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)  
        
        uri12d = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=adv_alkis_verkehr&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WMS_AdV_konform_App/guest'
        name = 'Verkehr'
        lyr12d = QgsRasterLayer(uri12d, name, 'wms')
        if not lyr12d.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr12d.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr12d, False)
            mygroup.addLayer(lyr12d)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)  
        
    def addWFS13(self):
        uri = 'https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WFS_OpenData/guest?&service=WFS&BBOX=1332412,6708967,1333423,6709355&restrictToRequestBBOX=1&VERSION=auto&typename=ave:Flurstueck&srsname=EPSG:25832&preferCoordinatesForWfsT11=false&pagingEnabled=true'
        name = 'LSA: ALKIS Flurstücke (WFS)'
        lyr13 = QgsVectorLayer(uri, name, 'WFS')
        if not lyr13.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr13.setOpacity(0.75) 
            lyr13.setMinimumScale(25000.0)
            lyr13.setMaximumScale(1.0)
            lyr13.setScaleBasedVisibility(1)
            # Farbe ändern
            lyr13.renderer().symbol().setColor(QColor("transparent"))
            lyr13.renderer().symbol().symbolLayer(0).setStrokeColor(QColor("black"))
            lyr13.renderer().symbol().symbolLayer(0).setStrokeWidth(0.2)
            lyr13.triggerRepaint() #braucht es nur wenn schon geladen
            # Legende updaten
            iface.layerTreeView().refreshLayerSymbology(lyr13.id())
            QgsProject.instance().addMapLayer(lyr13)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)

    def addWFS14(self):
        uri = 'https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_ALKIS_WFS_OpenData/guest?&service=WFS&BBOX=1332412,6708967,1333423,6709355&restrictToRequestBBOX=1&VERSION=auto&typename=ave:GebaeudeBauwerk&srsname=EPSG:25832&preferCoordinatesForWfsT11=false&pagingEnabled=true'
        name = 'LSA: ALKIS Gebäude (WFS)'
        lyr14 = QgsVectorLayer(uri, name, 'WFS')
        if not lyr14.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            # Opazität ändern
            lyr14.setOpacity(0.75)
            # Massstabsklassen/Sichtbarkeit ändern
            lyr14.setMinimumScale(25000.0)
            lyr14.setMaximumScale(1.0)
            lyr14.setScaleBasedVisibility(1)
            # Farbe ändern
            lyr14.renderer().symbol().setColor(QColor(220,220,220))
            lyr14.renderer().symbol().symbolLayer(0).setStrokeColor(QColor("black"))
            lyr14.renderer().symbol().symbolLayer(0).setStrokeWidth(0.1)
            lyr14.triggerRepaint() #braucht es nur wenn schon geladen
            # Legende updaten
            iface.layerTreeView().refreshLayerSymbology(lyr14.id())
            QgsProject.instance().addMapLayer(lyr14)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)
      
    def addWMS15(self):
        uri15 = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=Bauland&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_BRW2022_gast/guest'
        name = 'LSA: Bodenrichtwerte Bauland (WMS)'
        lyr15 = QgsRasterLayer(uri15, name, 'wms')
        if not lyr15.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr15.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr15)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)
        
    def addWMS93(self):
        uri93 = 'crs=EPSG:2398&dpiMode=7&format=image/png&layers=DSGK&styles&tilePixelRatio=0&url=http://geodienste.halle.de/opendata/f398a5d8-9dce-cbbc-b7ae-7e1a7f5bf809'
        name = 'HAL: Digitale Stadtgrundkarte (WMS)'
        lyr93 = QgsRasterLayer(uri93, name, 'wms')
        if not lyr93.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr93.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr93)
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)
        
    def addWMS21(self):
        myroot = QgsProject.instance().layerTreeRoot()
        mygroup = myroot.insertGroup(0, 'LSA: Topograf. Karten farbig (WMS)')
        uri21a = 'contextualWMSLegend=0&crs=EPSG:25832&dpiMode=7&featureCount=10&format=image/png&layers=lsa_lvermgeo_dtk10_col_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 10 farbig (WMS)'
        lyr21a = QgsRasterLayer(uri21a, name, 'wms')
        if not lyr21a.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr21a.setMinimumScale(17500.0)
            lyr21a.setMaximumScale(1.0)
            lyr21a.setScaleBasedVisibility(1)
            lyr21a.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr21a, False)
            mygroup.addLayer(lyr21a) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri21b = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk25_col_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 25 farbig (WMS)'
        lyr21b = QgsRasterLayer(uri21b, name, 'wms')
        if not lyr21b.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr21b.setMinimumScale(37500.0)
            lyr21b.setMaximumScale(17500.0)
            lyr21b.setScaleBasedVisibility(1)
            lyr21b.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr21b, False)
            mygroup.addLayer(lyr21b) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri21c = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk50_col_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 50 farbig (WMS)'
        lyr21c = QgsRasterLayer(uri21c, name, 'wms')
        if not lyr21c.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr21c.setMinimumScale(75000.0)
            lyr21c.setMaximumScale(37500.0)
            lyr21c.setScaleBasedVisibility(1)
            lyr21c.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr21c, False)
            mygroup.addLayer(lyr21c) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri21d = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk100_col_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 100 farbig (WMS)'
        lyr21d = QgsRasterLayer(uri21d, name, 'wms')
        if not lyr21d.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr21d.setMinimumScale(175000.0)
            lyr21d.setMaximumScale(75000.0)
            lyr21d.setScaleBasedVisibility(1)
            lyr21d.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr21d, False)
            mygroup.addLayer(lyr21d) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri21e = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=TUEK_250_col&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TÜK 250 farbig (WMS)'
        lyr21e = QgsRasterLayer(uri21e, name, 'wms')
        if not lyr21e.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr21e.setMinimumScale(5000000.0)
            lyr21e.setMaximumScale(175000.0)
            lyr21e.setScaleBasedVisibility(1)
            lyr21e.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr21e, False)
            mygroup.addLayer(lyr21e) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)
    def addWMS22(self):
        myroot = QgsProject.instance().layerTreeRoot()
        mygroup = myroot.insertGroup(0, 'LSA: Topograf. Karten grau (WMS)')
        uri22a = 'contextualWMSLegend=0&crs=EPSG:25832&dpiMode=7&featureCount=10&format=image/png&layers=lsa_lvermgeo_dtk10_ein_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 10 grau (WMS)'
        lyr22a = QgsRasterLayer(uri22a, name, 'wms')
        if not lyr22a.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr22a.setMinimumScale(17500.0)
            lyr22a.setMaximumScale(1.0)
            lyr22a.setScaleBasedVisibility(1)
            lyr22a.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr22a, False)
            mygroup.addLayer(lyr22a) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri22b = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk25_ein_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 25 grau (WMS)'
        lyr22b = QgsRasterLayer(uri22b, name, 'wms')
        if not lyr22b.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr22b.setMinimumScale(37500.0)
            lyr22b.setMaximumScale(17500.0)
            lyr22b.setScaleBasedVisibility(1)
            lyr22b.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr22b, False)
            mygroup.addLayer(lyr22b) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri22c = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk50_ein_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 50 grau (WMS)'
        lyr22c = QgsRasterLayer(uri22c, name, 'wms')
        if not lyr22c.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr22c.setMinimumScale(75000.0)
            lyr22c.setMaximumScale(37500.0)
            lyr22c.setScaleBasedVisibility(1)
            lyr22c.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr22c, False)
            mygroup.addLayer(lyr22c) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri22d = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=lsa_lvermgeo_dtk100_ein_1&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TK 100 grau (WMS)'
        lyr22d = QgsRasterLayer(uri22d, name, 'wms')
        if not lyr22d.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr22d.setMinimumScale(175000.0)
            lyr22d.setMaximumScale(75000.0)
            lyr22d.setScaleBasedVisibility(1)
            lyr22d.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr22d, False)
            mygroup.addLayer(lyr22d) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        

        uri22e = 'crs=EPSG:25832&dpiMode=7&format=image/png&layers=TUEK_250_grau&styles&tilePixelRatio=0&url=https://www.geodatenportal.sachsen-anhalt.de/wss/service/ST_LVermGeo_DTK_WMS_OpenData/guest?VERSION%3D1.3.0'
        name = 'LSA: TÜK 250 grau (WMS)'
        lyr22e = QgsRasterLayer(uri22e, name, 'wms')
        if not lyr22e.isValid():
            iface.messageBar().pushCritical(self.myPluginV, myCritical_1 + name + myCritical_2)        
        else:
            lyr22e.setMinimumScale(5000000.0)
            lyr22e.setMaximumScale(175000.0)
            lyr22e.setScaleBasedVisibility(1)
            lyr22e.renderer().setOpacity(0.75)
            QgsProject.instance().addMapLayer(lyr22e, False)
            mygroup.addLayer(lyr22e) 
            iface.messageBar().pushInfo(self.myPluginV, self.myInfo_1 + name + self.myInfo_2)        
