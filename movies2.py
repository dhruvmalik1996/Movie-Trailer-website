import movies1  #to import file movies1 in which our class movies is present
import fresh_tomatoes

Jump_Street_21 = movies1.movies("21 JUMP STREET", "https://images-na.ssl"
                                "-images-amazon.com/images/M/MV5BMTc3NzQ"
                                "3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._"
                                "V1_QL50_.jpg", "A pair of underachieving"
                                "cops are sent back to a local high school"
                                "to blend in and bring down a synthetic"
                                "drug ring.", "https://www.youtube.com/watch"
                                "?v=nfkiFVhiIYw")
Jump_Street_22 = movies1.movies("22 JUMP STEET", "https://images-na.ssl-"
                                "images-amazon.com/images/M/MV5BMTcwNzAx"
                                "MDU1M15BMl5BanBnXkFtZTgwNDE2NTU1MTE@._V1"
                                "_QL50_SY1000_CR0,0,674,1000_AL_.jpg", "After"
                                "making their way through high school"
                                "(twice), big changes are in store for officers"
                                "Schmidt and Jenko when they go deep undercover"
                                "at a local college.", "https://www.youtube.com/"
                                "watch?v=qP755JkDxyM")
Game_Of_Thrones = movies1.movies("GAME OF THRONES", "https://images-na.ssl-"
                                 "images-amazon.com/images/M/MV5BMjM5OTQ1MTY"
                                 "5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_QL50_"
                                 "SY1000_CR0,0,674,1000_AL_.jpg", "Winter Is"
                                 "Coming", "https://www.youtube.com/watch?v=iGp"
                                 "_N3Ir7Do")
Shawshank_Redemption = movies1.movies("SHAWSHANK REDEMPTION", "https://images"
                                      "-na.ssl-images-amazon.com/images/M/MV5"
                                      "BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2M"
                                      "jEyMDE@._V1_QL50_SY1000_CR0,0,672,1000_"
                                      "AL_.jpg", "Two imprisoned men bond over"
                                      "a number of years, finding solace and"
                                      "eventual redemption through acts of"
                                      "common decency.", "https://www.youtube."
                                      "com/watch?v=6hB3S9bIaco")
Deadpool = movies1.movies("DEADPOOL", "https://images-na.ssl-images-amazon.com/"
                          "images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3N"
                          "zE@._V1_QL50_SY1000_SX686_AL_.jpg", "A fast-talking mercen"
                          "ary with a morbid sense of humor is subjected to a rogue"
                          "experiment that leaves him with accelerated healing powers"
                          "and a quest for revenge.", "https://www.youtube.com/watch?v="
                          "ZIM1HydF9UA&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%"
                          "3DZIM1HydF9UA&has_verified=1")

L = [Jump_Street_21, Jump_Street_22, Game_Of_Thrones, Shawshank_Redemption, Deadpool]
fresh_tomatoes.open_movies_page(L)
