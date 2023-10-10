# Final solution to RuCode 7.0

 # 🚀 What is RuCode?

RuCode is an AI competition among students which is held by MIPT university, Yandex, Sber and Ministry of science and higher education of the Russian Federation.

## ✍️ What was the task this year?

Normalization of synthetically generated addresses.

# 🏆 What is our result?

🥈 2 place, ~ 0.9999 F1 score.

# 💾 Data

We had about 15kk addresses for training. About 5kk for prediction on public leaderbord and 5kk on private dataset. 3 days before the end of the competition we received a private dataset. As we found out, the public dataset perfectly correlated with public and private datasets.

# 💻 Solution

Having carried out a statistical analysis of the first words in synthetically generated addresses, I realized that they almost always uniquely determine the type of a particular subject. Having written a class that would transform this statistical knowledge into normalized addresses, I received a high score on the leaderboard and settled on this solution.
