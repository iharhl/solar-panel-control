## Get coordinates of objects

def get_coords_panel(canvas, solar_panel) -> tuple:
    xyPanel: tuple = canvas.coords(solar_panel)
    xPanel: int = (xyPanel[0]+xyPanel[2])//2
    yPanel: int = (xyPanel[1]+xyPanel[3])//2
    return (xPanel, yPanel)

def get_coords_sun(canvas, sun) -> tuple:
    xySun: tuple = canvas.coords(sun)
    xSun: int = (xySun[0]+xySun[2])//2
    ySun: int = (xySun[1]+xySun[3])//2
    return (xSun, ySun)