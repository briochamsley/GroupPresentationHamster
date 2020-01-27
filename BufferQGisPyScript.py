from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterNumber
from qgis.core import QgsProcessingParameterFeatureSink
import processing

#Set Workspace, so you need to change only this path if you're changing folders 
data_dir = "D:/Dokumente/Uni/FOSS/Data/"

class Model(QgsProcessingAlgorithm):
        
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterNumber('distance', 'Distance', type=QgsProcessingParameterNumber.Double, defaultValue=250))
        self.addParameter(QgsProcessingParameterFeatureSink('Railbuffered', 'RailBuffered', type=QgsProcessing.TypeVectorPolygon, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Roadbuffered', 'RoadBuffered', type=QgsProcessing.TypeVectorPolygon, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Buildingbuffered', 'BuildingBuffered', type=QgsProcessing.TypeVectorPolygon, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # BufferRails
        alg_params = {
            'DISSOLVE': True,
            'DISTANCE': parameters['distance'],
            'END_CAP_STYLE': 0,
            'INPUT': data_dir+'Rail.gpkg',
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': data_dir+'RailBuffered.gpkg'
        }
        outputs['Bufferrails'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Railbuffered'] = outputs['Bufferrails']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # BufferRoads
        alg_params = {
            'DISSOLVE': True,
            'DISTANCE': parameters['distance'],
            'END_CAP_STYLE': 0,
            'INPUT': data_dir+'Roads.gpkg',
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': data_dir+'RoadsBuffered.gpkg'
        }
        outputs['Bufferroads'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Roadbuffered'] = outputs['Bufferroads']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # BufferBuildings
        alg_params = {
            'DISSOLVE': True,
            'DISTANCE': parameters['distance'],
            'END_CAP_STYLE': 0,
            'INPUT': data_dir+'Buildings.gpkg',
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 2,
            'SEGMENTS': 5,
            'OUTPUT': data_dir+'BuildingsBuffered.gpkg'
        }
        outputs['Bufferbuildings'] = processing.run('native:buffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Buildingbuffered'] = outputs['Bufferbuildings']['OUTPUT']
        return results

    def name(self):
        return 'model'

    def displayName(self):
        return 'model'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Model()
