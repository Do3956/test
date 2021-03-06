# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

from a2 import *



if __name__ == '__main__':
	arr = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
		[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
		[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
		[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	]
	d5 = arraytogrid(arr)
	draw_grid(d5, width=3, number=d5.weights)

	print('\n')
	came_from, cost_so_far = bfs_search(d5, (1, 2), (4, 7))
	#draw_grid(diagram1, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
	print('\n')
	draw_grid(d5, width=3, number=cost_so_far, start=(1, 2), goal=(4, 7))
	print('\n')
	draw_grid(d5, width=3, path=reconstruct_path(came_from, start=(1, 2), goal=(4, 7)))




