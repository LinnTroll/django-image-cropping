from sorl.thumbnail.engines.pil_engine import Engine

class CropEngine(Engine):
    def scale(self, image, geometry, options):
        if options.get('box'):
            return image
        return super(CropEngine, self).scale(image, geometry, options)


    def crop(self, image, geometry, options):
        if options.get('box'):
            box = map(int, options.pop('box').split(','))
            image = image.crop(box)
            image = self.scale(image, geometry, options)
            return super(CropEngine, self).crop(image, geometry, options)
        else:
            return super(CropEngine, self).crop(image, geometry, options)