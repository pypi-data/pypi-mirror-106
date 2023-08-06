__version__ = "0.1.0"
__author__ = 'Henry Taylor'
__authoremail__ = 'henrysrtaylor@gmail.com'


#######################################################################################################
# Import Libraries
#######################################################################################################

from PIL import Image
import glob
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import re
import pyglet
import os
from shutil import rmtree
import numpy as np

#######################################################################################################
# Setup
#######################################################################################################

colors_default_list = ['yellow', 'red', 'blue', 'green', 'pink', 'purple', 'cyan', 'black', 'brown', 'navy', 'lawngreen', 'grey', 'tan', 'gold', 'darkred', 'turquoise', 'yellow', 'red', 'blue', 'green', 'pink', 'purple', 'cyan', 'black', 'brown', 'navy', 'lawngreen', 'grey', 'tan', 'gold', 'darkred', 'turquoise', 'yellow', 'red', 'blue', 'green', 'pink', 'purple', 'cyan', 'black', 'brown', 'navy', 'lawngreen', 'grey', 'tan', 'gold', 'darkred', 'turquoise']

desktop_file_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
print(desktop_file_path)

#######################################################################################################
# Functions: Backend
#######################################################################################################

def atoi(text):
        """Returns text converted to integer."""
        return int(text) if text.isdigit() else text

def natural_keys(text):
        """Orders converted text into natural integer ordering."""
        return [atoi(c) for c in re.split('(\d+)',text)]

def display_gif(file_path="C:\\Users\\Henry\\Desktop\\DataScience\\PYprojects\\GIFgraph\\doggy.gif", window_name= "Animated Graph"):
        """Displays GIF if option is selected.
        Parameters: 
                file_path - Where GIF is saved.
                window_name - Name of window on show.
        """
        window_text=f"GIFgraph: {window_name}"
        
        ani = pyglet.image.load_animation(file_path)
        anisprite = pyglet.sprite.Sprite(ani)

        w = anisprite.width
        h = anisprite.height

        window = pyglet.window.Window(w, h, window_text)
        icon = pyglet.image.load('graph_icon.png')
        window.set_icon(icon)

        r,g,b,alpha = 0.5,0.5,0.8,0.5
        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
                window.clear()
                anisprite.draw()

        pyglet.app.run()

def animate_frames(name:str, type:str, milsec:int, loop:int, folder_to_store_frames:str, folder_to_create:str, show_GIF:bool, easter_egg:bool):
    """Creates GIF from frames provided. Option to display GIF.        
    Parameters: 
                name - title of GIF.
                type - graph type to be generated as GIF.
                milsec - miliseconds between each frame.
                loop - Loop type, 0 is infinite, loop > 0 sets loop for that amount. This only applies to saved GIF. If show_GIF=True then GIF that displays will be infinite. 
                folder_to_store_frames - folder where frames are stored.
                folder_to_create - folder where GIF will be saved.
                show_GIF - Bool, True or False.
        """

    #### Sort Frames and Store in List ####  
    imgs = glob.glob(f"{folder_to_store_frames}\\\\{name}_{type}_Frame_*.jpeg") 
    imgs.sort(key=natural_keys)

    frames = []
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    #### Animate and Save as GIF ####    
    frames[0].save(f'{folder_to_create}\\GIFS\\{name}.gif', format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=milsec, loop=loop)
    
    #### Display or not ####  
    if show_GIF == True:
        if easter_egg == True:
            display_gif(window_name="Easter_Egg")
        else:
            display_gif(file_path=f'{folder_to_create}\\GIFS\\{name}.gif',window_name=name)

def ensure_dir(file_path):
    """Ensures folder structures are created if they do not already exist.
        Parameters: 
                file_path - Root folder where folder structure will be created.
        """
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        os.makedirs(file_path + "\\\\Frames")
        os.makedirs(file_path + "\\\\GIFS")

def ensure_dir_subfolder(file_path_subfolder):
        """Ensures specific folder for frames are there, deletes and recreates subfolder if not. Folder located at {file_path}\GIFgraph\Frames\{name}.
Parameters: 
        file_path - Root folder where folder structure will be created."""
        if os.path.exists(file_path_subfolder):
                rmtree(file_path_subfolder)
        os.makedirs(file_path_subfolder)
        

def iterate(top, step):
    """
    Iterates over data and creates upper limit so that more than one data point can be shown per frame. Controlled via step parameter.
        Parameters: 
                top - upper limit
                step - how many data points per frame specified by user
    
    """
    ht = list(range(0,len(top),step))
    # This causes the upper iteration limit to exceed total len range. 
    last_num = 2*len(top)
    ht.append(last_num)
    
    return ht


#######################################################################################################
# Functions: Graphs
#######################################################################################################

##### Line #####

def frames_line(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames):
    """Creates frames for line graphs.
        Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                folder_to_store_frames - Folder where each frame is stored.
        """
    x_list=[]
    y_list=[]

    iteration_list_upper_limits = iterate(y, step)

    # for i in iteration_list_upper_limits:
    #     y_list[0:i] = y[0:int(i)]

    for i in iteration_list_upper_limits:
        x_list = x[0:int(i)]
        y_list = y[0:int(i)]

        fig, ax = plt.subplots(figsize=size, dpi=dpi)
        ax.plot(x_list, y_list)
        ax.set(xlabel=f'{xname}', ylabel=f'{yname}',
            title=f'{name}')
        ax.set_ylim(4/5*min(y), 6/5*max(y))

        # Line can be string or numeric on x, so must account for both cases.
        if str(x[0]).isnumeric():
            ax.set_xlim(4/5*min(x), 6/5*max(x))
        else:
            ax.set_xlim(-0.5, (len(x)-0.5))
            xtick_loc = list(range(0,len(x),1))
            ax.set_xticks(xtick_loc)
            ax.set_xticklabels(x)

        plt.xticks(rotation=xrotation, fontweight='light', fontsize='small')

        imgnum = int(i+1)       
        plt.savefig(f'{folder_to_store_frames}\\{name}_Line_Frame_{imgnum}.jpeg')
        plt.close(fig)


def GG_line(x:object, y:object, xname:str="x_axis", yname:str="y_axis", name:str="title", step:int=1, size:tuple=(10,7), dpi:int=70, xrotation:int=0, milsec:int=400, loop:int=0, file_path:str=desktop_file_path, show_GIF:bool=True, easter_egg:bool=False):
    """Creates GIF from frames created. Option to display GIF.        
    Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                milsec - miliseconds between each frame.
                loop - Loop type, 0 is infinite, loop > 0 sets loop for that amount. This only applies to saved GIF. If show_GIF=True then GIF that displays will be infinite. 
                file_path - Folder where file structure will be created.
                show_GIF - Bool, True or False.
        """
    #### Folder Paths ####
    folder_to_create = (file_path + "\GIFgraph").replace("\\", "\\\\")
    ensure_dir(folder_to_create)

    folder_to_store_frames = folder_to_create + "\\\\Frames" + f"\\\\{name}"
    ensure_dir_subfolder(folder_to_store_frames)

    #### Create Frames ####            
    frames_line(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames)

    #### animate GIF ####  
    animate_frames(name=name, type="Line", milsec=milsec, loop=loop, folder_to_store_frames=folder_to_store_frames, folder_to_create=folder_to_create, show_GIF=show_GIF, easter_egg=easter_egg)


##### Bar #####

def frames_bar(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames):
    """Creates frames for bar graphs.
        Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                folder_to_store_frames - Folder where each frame is stored.
        """
    # Set x_list equal to x as we want each frame to show all x values
    x_list = [str(xi) for xi in x]
    # Set y_list equal to 0 as we want each frame to have another iteration of y
    y_list = [0 for i in range(len(x))]

    iteration_list_upper_limits = iterate(y, step)

    for i in iteration_list_upper_limits:
        y_list[0:i] = y[0:int(i)]

        fig, ax = plt.subplots(figsize=size, dpi=dpi)
        ax.bar(x_list, y_list)
        ax.set(xlabel=f'{xname}', ylabel=f'{yname}',
            title=f'{name}')
        ax.set_ylim(4/5*min(y), 6/5*max(y))
        ax.set_xlim(-0.75, len(x))
        plt.xticks(rotation=xrotation, fontweight='light', fontsize='small')

        imgnum = int(i+1)       
        plt.savefig(f'{folder_to_store_frames}\\{name}_Bar_Frame_{imgnum}.jpeg')
        plt.close(fig)

def GG_bar(x:object, y:object, xname:str="x_axis", yname:str="y_axis", name:str="title", step:int=1, size:tuple=(10,7), dpi:int=70, xrotation:int=0, milsec:int=400, loop:int=0, file_path:str=desktop_file_path, show_GIF:bool=True, easter_egg:bool=False):
    """Creates GIF from frames created. Option to display GIF.        
    Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                milsec - miliseconds between each frame.
                loop - Loop type, 0 is infinite, loop > 0 sets loop for that amount. This only applies to saved GIF. If show_GIF=True then GIF that displays will be infinite. 
                file_path - Folder where file structure will be created.
                show_GIF - Bool, True or False.
        """
    #### Folder Paths ####
    folder_to_create = (file_path + "\GIFgraph").replace("\\", "\\\\")
    ensure_dir(folder_to_create)

    folder_to_store_frames = folder_to_create + "\\\\Frames" + f"\\\\{name}"
    ensure_dir_subfolder(folder_to_store_frames)

    #### Create Frames ####            
    frames_bar(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames)

    #### animate GIF ####  
    animate_frames(name=name, type="Bar", milsec=milsec, loop=loop, folder_to_store_frames=folder_to_store_frames, folder_to_create=folder_to_create, show_GIF=show_GIF, easter_egg=easter_egg)


#### Scatter ####

def frames_scatter(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames):
    """Creates frames for bar graphs.
        Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                folder_to_store_frames - Folder where each frame is stored.
        """    
        
    iteration_list_upper_limits = iterate(x, step)

    for i in iteration_list_upper_limits:
        x_list = x[0:int(i)]
        y_list = y[0:int(i)]

        fig, ax = plt.subplots(figsize=size, dpi=dpi)
        ax.scatter(x_list, y_list)
        ax.set(xlabel=f'{xname}', ylabel=f'{yname}',
            title=f'{name}')
        ax.set_ylim(4/5*min(y), 6/5*max(y))

        x_scale_increase = (max(x)/66)
        ax.set_xlim(min(x) - x_scale_increase, max(x) + x_scale_increase)
        plt.xticks(rotation=xrotation, fontweight='light', fontsize='small')

        imgnum = int(i+1)       
        plt.savefig(f'{folder_to_store_frames}\\{name}_Scatter_Frame_{imgnum}.jpeg')
        plt.close(fig)

def GG_scatter(x:object, y:object, xname:str="x_axis", yname:str="y_axis", name:str="title", step:int=1, size:tuple=(10,7), dpi:int=70, xrotation:int=0, milsec:int=400, loop:int=0, file_path:str=desktop_file_path, show_GIF:bool=True, easter_egg:bool=False):
    """Creates GIF from frames created. Option to display GIF.        
    Parameters: 
                x - x-axis data.
                y - y-axis data.
                xname - x-axis name.
                yname - y-axis name.
                name - Title of GIF.
                step - How many data points to be plotted per frame.
                size - Size of GIF.
                dpi - Dots Per Inch.
                xrotation - Rotation of x-axis.
                milsec - miliseconds between each frame.
                loop - Loop type, 0 is infinite, loop > 0 sets loop for that amount. This only applies to saved GIF. If show_GIF=True then GIF that displays will be infinite. 
                file_path - Folder where file structure will be created.
                show_GIF - Bool, True or False.
        """
    #### Folder Paths ####
    folder_to_create = (file_path + "\GIFgraph").replace("\\", "\\\\")
    ensure_dir(folder_to_create)

    folder_to_store_frames = folder_to_create + "\\\\Frames" + f"\\\\{name}"
    ensure_dir_subfolder(folder_to_store_frames)

    #### Create Frames ####            
    frames_scatter(x, y, xname, yname, name, step, size, dpi, xrotation, folder_to_store_frames)

    #### animate GIF ####  
    animate_frames(name=name, type="Scatter", milsec=milsec, loop=loop, folder_to_store_frames=folder_to_store_frames, folder_to_create=folder_to_create, show_GIF=show_GIF, easter_egg=easter_egg)


    #### Pie ####

def frames_pie(x, y, name, explode, step, size, autopct, autopct_color, label_color, colors_list,legend, shadow, dpi, folder_to_store_frames):
    """Creates frames for pie graphs.
        Parameters: 
                x - x-axis data.
                y - y-axis data.
                name - Title of GIF.
                Explode - Distance of pie segments from each other.
                step - How many data points to be plotted per frame.
                autopct - Pie chart percentages. Add string based on formatting or None.
                autopct_color - Color of data labels. 
                label_color - Color of text labels ~ 'y'. 
                colors_list - list of colors to use for each pie segment. Accepts hex, and color names. Ensure number of colors >= number segments.
                legend - displays legend on chart.
                shadow - displays shadow under pie.
                size - Size of GIF.
                dpi - Dots Per Inch.
                folder_to_store_frames - Folder where each frame is stored.
        """    
    iterate_list = range(len(x))
    colours_list_temp = ['white' for x in iterate_list]
    labels_list_temp = ['' for x in iterate_list]
    legend_list = [mlines.Line2D([], [], color=colors_list[i], lw=5, ls='-', label=y[i]) for i in iterate_list]

    iteration_list_upper_limits = iterate(iterate_list, step)

    if explode == "Default_Value":
        explode = [0 for x in range(len(x))]
    else:
        pass
    
    for i in iteration_list_upper_limits:
        colours_list_temp[0:i] = colors_list[0:i]
        labels_list_temp[0:i] = y[0:i]

        fig, ax = plt.subplots(figsize=size, dpi=dpi)
        patches, texts, autotexts  = ax.pie(x, labels=labels_list_temp, explode=explode, autopct = autopct, pctdistance=0.8, textprops={"weight":"bold"}, colors=colours_list_temp, shadow=shadow)
        
        if legend == True:
            plt.legend(handles=legend_list, title="Legend", bbox_to_anchor=(0.7, 0, 0.5, 1))
        else:
            pass

        # Sets autotexts to white and then resets them to color chosen by user (autopct_color) at each iteration.
        [autotext.set_color('white') for autotext in autotexts]
        [autotext.set_color(autopct_color) for autotext in autotexts[0:i]]

        [text.set_color(label_color) for text in texts]
        ax.set_title(name)

        imgnum = int(i+1)       
        plt.savefig(f'{folder_to_store_frames}\\{name}_Pie_Frame_{imgnum}.jpeg')
        plt.close(fig)

def GG_pie(x:object, y:object, name:str="title", explode:object="Default_Value", step:int=1, autopct:str='%1.1f%%', autopct_color:str="white", label_color:str="black", colors_list:list=colors_default_list, legend:bool=True, shadow:bool=False, size:tuple=(10,7), dpi:int=70, milsec:int=400, loop:int=0, file_path:str=desktop_file_path, show_GIF:bool=True, easter_egg:bool=False):
    """Creates GIF from frames created. Option to display GIF.        
    Parameters: 
                x - x-axis data.
                y - y-axis data.
                name - Title of GIF.
                Explode - Distance of pie segments from each other.
                step - How many data points to be plotted per frame.
                autopct - Pie chart percentages. Add string based on formatting or None.
                autopct_color - Color of data labels. 
                label_color - Color of text labels ~ 'y'. 
                colors_list - list of colors to use for each pie segment. Accepts hex, and color names. Ensure number of colors >= number segments. 
                legend - displays legend on chart.
                shadow - displays shadow under pie.
                size - Size of GIF.
                dpi - Dots Per Inch.
                milsec - miliseconds between each frame.
                loop - Loop type, 0 is infinite, loop > 0 sets loop for that amount. This only applies to saved GIF. If show_GIF=True then GIF that displays will be infinite. 
                file_path - Folder where file structure will be created.
                show_GIF - Bool, True or False.
        """
    #### Folder Paths ####
    folder_to_create = (file_path + "\GIFgraph").replace("\\", "\\\\")
    ensure_dir(folder_to_create)

    folder_to_store_frames = folder_to_create + "\\\\Frames" + f"\\\\{name}"
    ensure_dir_subfolder(folder_to_store_frames)

    #### Create Frames ####            
    frames_pie(x, y, name, explode, step, size, autopct, autopct_color, label_color, colors_list, legend, shadow, dpi, folder_to_store_frames)

    #### animate GIF ####  
    animate_frames(name=name, type="Pie", milsec=milsec, loop=loop, folder_to_store_frames=folder_to_store_frames, folder_to_create=folder_to_create, show_GIF=show_GIF, easter_egg=easter_egg)

