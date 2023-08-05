# -*- coding: utf-8 -*-
# @Organization  : insightface.ai
# @Author        : Jia Guo
# @Time          : 2021-05-04
# @Function      : 


from __future__ import division
import collections
import numpy as np
import glob
import os
import os.path as osp
from numpy.linalg import norm
from ..model_zoo import model_zoo
from ..utils import face_align

__all__ = ['FaceAnalysis', 'Face']

Face = collections.namedtuple('Face', [
    'bbox', 'landmark', 'det_score', 'embedding', 'gender', 'age',
    'embedding_norm', 'normed_embedding'
])

Face.__new__.__defaults__ = (None, ) * len(Face._fields)


class FaceAnalysis:
    def __init__(self, model_root_dir):
        self.models = {}
        onnx_files = glob.glob(osp.join(model_root_dir), '*.onnx')
        for onnx_file in onnx_files:
            model = model_zoo.get_model(onnx_file)
            self.models[model.taskname] = model
        assert 'detection' in self.models
        self.det_model = self.models['detection']
        self.det_size = self.det_model.input_size


    def prepare(self, ctx_id, det_thresh=0.5, det_size=(640, 640)):
        self.det_thresh = det_thresh
        if self.det_size is not None and det_size is not None:
            print('warning: det_size is already given in detection model')
        elif det_size is not None:
            self.det_size = det_size
        for taskname, model in self.models:
            model.prepare(ctx_id)

    def get(self, img, det_size=None, max_num=0):
        if det_size is None:
            det_size = self.det_size
        if det_size is None:
            det_size = (640, 640) #default det size
        bboxes, kpss = self.det_model.detect(img,
                                             threshold=self.det_thresh,
                                             input_size=det_size,
                                             max_num=max_num,
                                             metric='default')
        if bboxes.shape[0] == 0:
            return []
        ret = []
        for i in range(bboxes.shape[0]):
            bbox = bboxes[i, 0:4]
            det_score = bboxes[i, 4]
            kps = None
            if kpss is not None:
                kps = kpss[i]
            embedding = None
            normed_embedding = None
            embedding_norm = None
            gender = None
            age = None
            if 'recognition' in self.models:
                assert kps is not None
                rec_model = self.models['recognition']
                aimg = face_align.norm_crop(img, landmark=kps)
                embedding = None
                embedding_norm = None
                normed_embedding = None
                gender = None
                age = None
                embedding = rec_model.get_feat(aimg).flatten()
                embedding_norm = norm(embedding)
                normed_embedding = embedding / embedding_norm
            if 'genderage' in self.models:
                assert aimg is not None
                ga_model = self.models['genderage']
                gender, age = ga_model.get(_img)
            face = Face(bbox=bbox,
                        landmark=landmark,
                        det_score=det_score,
                        embedding=embedding,
                        gender=gender,
                        age=age,
                        normed_embedding=normed_embedding,
                        embedding_norm=embedding_norm)
            ret.append(face)
        return ret

