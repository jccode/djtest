from django.shortcuts import render_to_response
from models import Food, MPTTFood

def _display(foods):
    """
    
    Arguments:
    - `foods`:
    """
    display_list = []
    for food in foods:
        display_list.append(food.title)
        children = food.children.all()
        if len(children) > 0:
            display_list.append(_display(children))
    return display_list
    

def unordered_list(request):
    foods = Food.objects.filter(parent=None)
    str = _display(foods)
    return render_to_response('atest/foods.html', {'foods': str})
    

def mptttree_list(request):
    nodes = MPTTFood.objects.all()
    return render_to_response('atest/mpttfoods.html', {'nodes': nodes})
    
