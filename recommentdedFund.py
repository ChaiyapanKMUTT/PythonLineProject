import pickle



# Load the machine learning model and fund_tax_list
with open('model_recoment_fund.pkl', 'rb') as file:
    model, fund_tax_list = pickle.load(file)

# Function to recommend funds
def recommend_items(input_item, model, items_to_recommend):
    possible_items = fund_tax_list
    input_item = input_item.upper()
    if input_item in possible_items :
        predictions = [(input_item, item, model.predict(input_item, item).est) for item in possible_items if item not in input_item]
        recommendations = sorted(predictions, key=lambda x: x[2], reverse=True)[:items_to_recommend]
        recommended_items = [item for _, item, _ in recommendations]
    else :
        recommended_items = ['ไม่ใช่กองทุนภาษี']   
    return recommended_items

def input_fund(input_fund):
    input_item = input_fund
    recomment_item = recommend_items(input_item, model, 5)
    return recomment_item