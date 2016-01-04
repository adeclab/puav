# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


image = plt.imread( 'baker_adexl.png')


if __name__ == "__main__":
    arrow = dict(facecolor = 'black',
        arrowstyle = '->')

    fig, ax = plt.subplots()

    ax.annotate( "Zmienne",
        xy = ( 200, 450),
        textcoords = 'data', xytext = (350, 1050), size = 15,
        arrowprops = arrow)

    ax.annotate( "Symulacje",
        xy = ( 100, 200),
        textcoords = 'data', xytext = (750, 1050), size = 15,
        arrowprops = arrow)

    ax.annotate( "Wyniki symulacji",
        xy = ( 550, 500),
        textcoords = 'data', xytext = (1250, 800), size = 15,
        arrowprops = arrow)

    ax.annotate( "Przycisk uruchomienia symulacji",
        xy = ( 620, 115),
        textcoords = 'data', xytext = (800, 115), size = 15,
        arrowprops = arrow)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.imshow(image)
    plt.show()
