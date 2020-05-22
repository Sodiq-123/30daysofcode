def make_car(manufacturer=None, model=None, **car):
    return {'manufacturer':manufacturer, 'model':model, **car}
print(make_car('subaru', 'outback', color='blue', tow_package=True))