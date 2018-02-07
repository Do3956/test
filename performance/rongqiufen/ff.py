# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

from a2 import *



if __name__ == '__main__':
	arr = [
		[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
		[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
		[1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
		[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	]
	d5 = arraytogrid(arr)
	draw_grid(d5, width=3, number=d5.weights)


	rst = floodfill(d5, (2, 2), 1, 2)
	print('\n')
	draw_grid(rst, width=3, number=rst.weights)


	rst = floodfill(d5, (4, 7), 1, 5)
	print('\n')
	draw_grid(rst, width=3, number=rst.weights)
