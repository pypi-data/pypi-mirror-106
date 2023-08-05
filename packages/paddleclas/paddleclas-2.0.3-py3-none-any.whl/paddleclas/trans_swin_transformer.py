import paddle
import torch
import numpy as np

def trans(name):
    input_fp = "./torch_pretrain/{}.pth".format(name)
    output_fp = "./swin_pretrain/{}.pdparams".format(name.replace("swin", "SwinTransformer")+"_pretrained")

    torch_dict = torch.load(input_fp)["model"]
    paddle_dict = {}
    fc_names = ["qkv.weight", "fc1.weight", "fc2.weight", "downsample.reduction.weight", "head.weight", "attn.proj.weight"]
    for key in torch_dict:
        weight = torch_dict[key].cpu().numpy()
        flag = [i in key for i in fc_names]
        if any(flag):
            print("weight {} need to be trans".format(key))
            weight = weight.transpose()
        paddle_dict[key] = weight

    paddle.save(paddle_dict, output_fp)
    print("ok")
    return

if __name__ == "__main__":
    names = ["swin_base_patch4_window7_224_22k", "swin_base_patch4_window7_224_22kto1k", "swin_base_patch4_window12_384_22k", "swin_base_patch4_window12_384_22kto1k", "swin_large_patch4_window7_224_22k", "swin_large_patch4_window7_224_22kto1k", "swin_large_patch4_window12_384_22k", "swin_large_patch4_window12_384_22kto1k"]
    for name in names:
        trans(name)
