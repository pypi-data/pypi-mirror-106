DEFAULT_TILE_SIZES = [1, 3, 4]

def get_tile(grid_step, coords, image_input):
    start = tf.cast(tf.math.floor(coords * grid_step))
    end = tf.cast(tf.math.ceil((coords + 1) * grid_step))

    return image_input[start[0]:end[0], start[1]:end[1], :]

def averaged_pixels_for_tile(image_tile):
    return tf.math.reduce_mean(image_tile, axis=[0, 1])

def level_histogram_for_tile(image_tile):
    pass

def gradient_histogram_for_tile(image_tile):
    pass

def features_for_tiles(tile_sizes, tile_processor, input_image):
    features = []

    for tsize in tile_sizes:
        h_step = tf.shape(input_image)[0] / tsize
        w_step = tf.shape(input_image)[1] / tsize

        for i in range(tsize):
            for j in range(tsize):
                atile = get_tile((h_step, w_step), (i, j), input_image)
                features.append(tile_processor(atile))

    tf.concat(features, -1)
