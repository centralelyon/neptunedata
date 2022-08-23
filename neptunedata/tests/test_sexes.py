from neptunedata.models import Sexes

def test_sexes():

  assert isinstance(Sexes.get_sexes(), dict), "should be a dict"