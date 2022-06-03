import numpy as np
from flask import Flask,render_template,request
import pickle,pandas
popular_df=pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_score=pickle.load(open('similarity_score.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['No_of_ratings'].values),
                           rating=list(np.round_(popular_df['Avg_rating'].values)))
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['Post'])
def recommend():

    user_input=request.form.get('book_name')
    print("Value should be 4 Blondes or (array([3]),) ")
    print(np.where(pt.index == user_input))
    index = np.where(pt.index == user_input)[0][0]
    print("printing the value of index")
    print(index)

    similar_item = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    print("Similar_item: ",similar_item)
    data = []
    for i in similar_item:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    print(data)
    return render_template("recommend.html",data=data)

@app.route('/click_recommend')
def click_recommend():

    return render_template("click_recommend.html")


if __name__=='__main__':
    app.run(debug=True,port=5000)





