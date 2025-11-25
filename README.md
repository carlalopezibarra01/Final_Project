# Final_Project
Group members:
Carla López-Ibarra: carlalopezibarra01
Àfrica Oltra: africaoltra
Manel Paredes: manelparedes01
Marc Sanchez: Marc-Sanchez13

Download links of the data:
bcn_listings= https://data.insideairbnb.com/spain/catalonia/barcelona/2025-06-12/data/listings.csv.gz 
mad_listings= https://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2025-06-12/data/listings.csv.gz 

Additional information relevant for when reviewing your project:
    1) When selecting the rule for the second version of "graph2", we noticed that in its first version, the average rate per area over time remains constant. This happens because, according to the project’s model definition, the nightly rates for each listing are set only once, when each Place runs its .setup(). In other words, the rates do not change over time in the original version of the model; each property has a fixed rate that is never updated during the 180 months. This doesn’t make much sense, because if we want to create a chart of “average rate per area over time,” we should implement some rule that modifies prices on a monthly basis. We chose that, after each sale, the price is revalued randomly using the following command:

    place.rate = place.rate * random.uniform(0.95, 1.15)

    2) For the second part of the project, we are answering question 1:
    "Are listings controlled by few hosts?". For that, we are comparing 2 big cities of Spain: Madrid and Barcelona. Both dataframes contain information from June 2025.