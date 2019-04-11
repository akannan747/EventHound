# Midterm report
### This report should in detail explain your Minimum Viable Project (baseline solution) and it should include an evaluation of how well your solution performs on the problem you're trying to solve. The report should clearly outline the progress you have made so far, as well as the challenges you are currently facing.

### Also include a link to your Github repository where you have all the code base that you have produced in your project. 

 

### Here are a few things you should include and explain in your report

### 1. Datasets you're using: Eventbrite and Ticketmaster
### 2. Data analysis / EDA results: Expected outcome: Based on user query and the descriptions of the events, we hope to provide a top five list of events that the user would be interested in. Events considered would be within a five mile radius of the target location as well as within the requested time frame or within a month of the search. 
### 3. Baseline models that are trained on your data you have (this might not be the best model, but should give you an idea about the next steps)
### 4. A link to a working prototype of your full system, preferably with an interactive UI (with backend and frontend connected). Note, this might not be the final version or have all the functionalities - include screenshots or a link to a video of a screen recording where you walk through the system
### 5. Performance evaluation. Answer the question: "Are you currently satisfied with your system's performance". Why / why not?)
### 6. System Architecture Overview (in detail) -- if it's a system where a user interacts also outline the UX interaction flow + Code snippets to explain certain parts of the work done
### 8. Key findings
### 9. Bottlenecks / challenges

## __TM to DF Code.ipynb__
### Ticketmaster dataset
### __Method__: Web scraping
### Found events under postal code 90703, 94704
### Variables to consider: 
name','venues','pleasenote', 'type', 'genre', 'subGenre', 'info','pleaseNote','sales', 'classifications']

### __Results__: 27 listings of which all were related to music or arts and theatre. The three main events: The Secret Garden theatre showing, Shrek the Musical, and a series of concerts/music shows would not provide the variety necessary to encompass the range of events that would be sought after on an event finder, nor does it span people’s general interests. Also, these 27 listings would not be sufficient in training a model. 

## word2vec.ipynb
#### Eventbrite dataset
### To supplement our data, we looked into Eventbrite, another event source with event descriptions, ratings, and events catered towards an expanded range of interests.
### Without being able to access private event attendance records and train them on individuals’ reviews from Ticketmaster alone, we would not be able to personalize event findings as we initially planned to. With this limited data dilemma in mind, we adjusted our feasible, short-term expected outcome to procure a list of the top five most popular events in the area, similar to a google query. We hoped that generalizing the search results and providing multiple options would increase the likelihood of users finding an event they would be interested in. 
### Therefore, for the next steps, we decided to use word2vec to compare user queries to the event descriptions to provide users the top search results. Our goal was to group similar words and train them to correlate to the average rating of an event. 
### In order for this method to be implemented, we first needed a large batch of text data drawn from a relevant domain. After collecting the reviews, we pre-processed the file to return a list of words as tokens. The resulting data file held about 10,000 entries of 100+ words per entry, which gave us over a million words to use. From there, the tokens were trained with a neural network with a single hidden layer. The weights of the instances were then recorded to determine the degree of similarity between words. 
### Example with “drink”:
![](/Downloads/drinknlp.png )

Performance Evaluation/Challenges:
Currently our algorithm is designed for one-word queries, likened to the example above with the word “drink”, where we count the number of “similar words”, which are words that reach a certain level of similarity to the query. The way that our algorithm is designed, it will look for the highest rate of the occurrence of the query word per word within a description. This is definitely a start for us. With some tinkering of our model, it will be able to the description with the most occurrences of words like the query word. However, considering the goal of our project, this serves mostly as a foundation for us to work upon. 
First off, queries are usually more than one word. We do plan to strip voice-recognized queries of words such as “the” and “a” which don’t give much insight. However, we will need to adjust our algorithm to be able to take into queries that are longer than one word. There are different avenues that we could take into regard with that. Algorithms such as the bag-of-words algorithm exist, or a more rudimentary and less effective method could be to run the current algorithm for each important word in the query.
Also, 


One of the challenges that we encountered was the establishment of an evaluation metric. We realized that the idea in our head could’ve been done without any practical implementation of machine learning algorithms. This caused us to shift the implementation of our algorithm to take this into account. 
The main challenges that we are running into are related to the matter of evaluation. To know how good one’s model is, there is often an evaluation metric to measure how accurate that model is. However, with the way that our project is designed, it was difficult to establish what would be our form of evaluation. Our original proposal was to have Alexa be asked regarding events occuring in a certain area, and then to have it ask enough questions to be able to give recommendations. However, we were unclear of a good way to evaluate how “good” the event was. Some suggestions that came to mind were to look for the amount of people who went to similar events and to train off of that. That in itself would have been another problem to tackle, in part because a lot of the information that we deemed to be evaluation metrics were not available to us through the API. Through our considerations, we went with utilizing 
	Also, in consideration of our project, we realized that our previous view of how the project could have been implemented would have been without any usage of machine learning algorithms. It could’ve been as simple as just looking for events with certain words in it. However
	
Something that we will also need to consider moving forward is if it will be possible to be able to tailor events to a particular user’s tastes, as well as if we would want to do that. 

 



