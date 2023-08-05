from pollination.annual_radiation.entry import AnnualRadiationEntryPoint
from queenbee.recipe.dag import DAG


def test_annual_radiation():
    recipe = AnnualRadiationEntryPoint().queenbee
    assert recipe.name == 'annual-radiation-entry-point'
    assert isinstance(recipe, DAG)
