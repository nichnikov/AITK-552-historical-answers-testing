import os
import pandas as pd
import requests

queies_df = pd.read_csv(os.path.join("data", "bss_supp_queries.csv"), sep="\t")
# queies_df = pd.read_csv(os.path.join("data", "bss_supp_queries.csv"))
print(queies_df)
test_results = []
# for num, q in enumerate(queies_df["Query"].to_list()[:1000]):
for num, d in enumerate(queies_df.to_dict("records")[:1000]):
    print(num, d)
    q_request = {"pubid": 9, "text": d["Query"]}
    res = requests.post("http://0.0.0.0:8090/api/search", json=q_request)
    res_dict = res.json()
    test_results.append({**d, **res_dict})

test_results_df = pd.DataFrame(test_results)
print(test_results_df)
test_results_df.to_csv(os.path.join("results", "AITK552_task_test_exp_all_1000.csv"), sep="\t", index=False)