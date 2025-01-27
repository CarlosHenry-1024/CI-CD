from transformers import pipeline

# 加载情感分析模型
local_model_path = "/Users/a1-6/ptj/test_web_model/transfomer"
nlp_pipeline = pipeline("sentiment-analysis", model=local_model_path, tokenizer=local_model_path)


def predict(text):
    # 获取标签映射
    label_map = nlp_pipeline.model.config.id2label
    result = nlp_pipeline(text)[0]

    # 获取预测标签
    label = result['label']

    # 将标签映射到实际情感标签
    actual_label = [k for k, v in label_map.items() if v == label][0]
    if actual_label == 0:
        actual_label = 'NEGATIVE'
    else:
        actual_label = 'POSITIVE'
    result['label'] = actual_label

    return result