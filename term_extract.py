# 双语术语提取工具
def extract_terms(source_file, target_file):
    with open(source_file, "r", encoding="utf-8") as f_src:
        src_lines = [line.strip() for line in f_src.readlines() if line.strip()]
    with open(target_file, "r", encoding="utf-8") as f_tgt:
        tgt_lines = [line.strip() for line in f_tgt.readlines() if line.strip()]

    term_pairs = []
    # 简单匹配：按行提取对应术语对
    min_len = min(len(src_lines), len(tgt_lines))
    for i in range(min_len):
        term_pairs.append({"英文术语": src_lines[i], "中文术语": tgt_lines[i]})
    return term_pairs

import pandas as pd
if __name__ == "__main__":
    pairs = extract_terms("source_term.txt", "target_term.txt")
    df = pd.DataFrame(pairs)
    df.to_excel("term_result.xlsx", index=False)
    print("术语提取完成，已输出 term_result.xlsx")
#（注：内容由AI生成）
