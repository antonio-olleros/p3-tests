"""
XBRL instance manager using Arelle

"""

from arelle import Cntlr
import pandas as pd

def load_xbrl_file(xbrl_file_path):
    """
    Load an XBRL instance file and return the model.
    """
    controller = Cntlr.Cntlr()
    controller.startLogging(logFileName='logToPrint')
    modelXbrl = controller.modelManager.load(xbrl_file_path)

    return modelXbrl, controller

def facts_to_dict(modelXbrl):
    """
    Extract facts from an XBRL instance file.
    """
    facts = []
    # Extract facts with dimensions
    for fact in modelXbrl.facts:
        fact_info = {
            'concept': fact.concept.qname,
            'value': fact.value if hasattr(fact, 'value') else fact.text,
            'unit': fact.unit.measures[0][0],
            'decimals': fact.decimals if hasattr(fact, 'decimals') else None,
            'period': fact.context.endDate,
            'entity': fact.context.entity.stringValue
        }
        
        for item in fact.context.scenario:
            fact_info[item.dimension.qname] = item.member.qname
        
        facts.append(fact_info)

    return facts

def facts_to_df(facts_dict):
    """
    Convert a list of facts to a pandas DataFrame.
    """
    return pd.DataFrame(facts_dict)

def instance_to_df(xbrl_file_path):
    """
    Convert an XBRL instance to a pandas DataFrame.
    """
    modelXbrl, controller = load_xbrl_file(xbrl_file_path)
    
    facts_dict = facts_to_dict(modelXbrl)

    modelXbrl.close()
    controller.close()

    return facts_to_df(facts_dict)