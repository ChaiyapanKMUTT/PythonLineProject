import pickle
# Load the machine learning model and fund_tax_list
with open('model_recoment_fund_d3.pkl', 'rb') as file:
    possible_items, cosine_sim = pickle.load(file)


def recommend_fund(input_item, n_item=5):
    input_item = input_item.upper()
    if input_item in possible_items.values :
      idx_fund = possible_items[possible_items['fund_name']==input_item].index[0]
      sim_scores = list(enumerate(cosine_sim[idx_fund]))
      sim_scores = sorted(sim_scores, key= lambda x: x[1] , reverse=True)[1:n_item+1]

      ic_indices = [i[0] for i in sim_scores]
      result = possible_items.filter(items=ic_indices, axis=0)
      recommended_items = result.fund_name.tolist()
      
    else :
        recommended_items = ['ไม่ใช่กองทุนภาษี']   
    return recommended_items