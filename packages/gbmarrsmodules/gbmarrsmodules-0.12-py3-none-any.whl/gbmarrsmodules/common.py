import re
import os

from rdflib import Namespace

from .util import getDataRoot 


def getDownDir(dataset, dataBuild):
    dataroot = getDataRoot("data", dataBuild) # this is the location where the data should be stored from the downloaded input and output of the ETLs
    downloaddir = os.path.join (dataroot, dataset, "download/")
    return downloaddir

def getRDFDir(dataset, dataBuild):
    dataroot = getDataRoot("data", dataBuild)
    rdfdir = os.path.join (dataroot, dataset, "rdf/")
    return rdfdir

def getSQLDir(dataset, dataBuild):
    dataroot = getDataRoot("data", dataBuild)
    sqldir = os.path.join (dataroot, dataset, "sql/")
    return sqldir

def getWorkDir(dataset, dataBuild):
    dataroot = getDataRoot("data", dataBuild)
    workdir = os.path.join (dataroot, dataset, "work/")
    return workdir


RELATE_DATA = Namespace ("http://generalbioinformatics.com/data/relate#")
RELATE_VOC = Namespace ("http://generalbioinformatics.com/ontologies/relate#")

CHEMBL_DATA = Namespace ("http://generalbioinformatics.com/data/chembl#")
CHEMBL_VOC = Namespace ("http://generalbioinformatics.com/ontologies/chembl#")

PROJECT_DATA = Namespace ("http://generalbioinformatics.com/data/project#")
PROJECT_VOC = Namespace ("http://generalbioinformatics.com/ontologies/project#")

PHENOTYPE_DATA = Namespace ("http://generalbioinformatics.com/data/phenotype#")
PHENOTYPE_VOC = Namespace ("http://generalbioinformatics.com/ontologies/phenotype#")

MAP_DATA = Namespace ("http://generalbioinformatics.com/data/idMapping#")
MAP_VOC = Namespace ("http://generalbioinformatics.com/ontologies/idMapping#")

def getCompoundUri(cid):
        """
                STITCH has two kinds of compounds ids
                Some are labelled stereochemical ids. They start with CID0... 
                 and are actually pubchem compound (not substance!) ids with CID, a zero, and more digits (nine in total).
                The others are flat ids, and start with CID, a one, and more digits (also nine in total).
                These do not seem to have a correspondence with PubChem.
        """
        cidPat = "^CID0*"
        if not (re.match (cidPat, cid)):
                raise Exception("" + cid + " doesn't match pattern CID\d+")
        cid = re.sub (cidPat, '', cid)
        return idPubchemCompound[cid]

