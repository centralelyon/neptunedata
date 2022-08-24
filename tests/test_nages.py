import sys
sys.path.append('./')
from neptunedata.models import Nages

def test_nages():
  assert isinstance(Nages.get_nages(), dict), "should be a dict"

def test_nages_unknown():
  assert "Unknown" in Nages.get_nages().keys(), "should have unknown key"