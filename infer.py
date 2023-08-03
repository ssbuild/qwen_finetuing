# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 15:29
import torch
from deep_training.data_helper import ModelArguments, TrainingArguments, DataArguments
from transformers import HfArgumentParser
from data_utils import train_info_args, NN_DataHelper
from aigc_zoo.model_zoo.qwen.llm_model import MyTransformer,QWenTokenizer,LoraArguments,setup_model_profile, QWenConfig



if __name__ == '__main__':
    train_info_args['seed'] = None
    parser = HfArgumentParser((ModelArguments, DataArguments,))
    model_args, data_args = parser.parse_dict(train_info_args,allow_extra_keys=True)

    setup_model_profile()

    dataHelper = NN_DataHelper(model_args, None, data_args)
    tokenizer: QWenTokenizer
    tokenizer, config, _,_ = dataHelper.load_tokenizer_and_config(
        tokenizer_class_name=QWenTokenizer, config_class_name=QWenConfig)

    pl_model = MyTransformer(config=config, model_args=model_args, torch_dtype=torch.float16,)

    model = pl_model.get_llm_model()
    model.half().cuda()
    model = model.eval()

    text_list = [
        "写一个诗歌，关于冬天",
        "晚上睡不着应该怎么办",
    ]
    for input in text_list:
        response, history = model.chat(tokenizer, input, history=[], max_length=2048,
                                       eos_token_id=config.eos_token_id,
                                       do_sample=True, top_p=0.7, temperature=0.95, )
        print("input", input)
        print("response", response)

    # response, history = base_model.chat(tokenizer, "写一个诗歌，关于冬天", history=[],max_length=30)
    # print('写一个诗歌，关于冬天',' ',response)

