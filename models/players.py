from tinydb import TinyDB, Query
from datetime import datetime


db = TinyDB("data/player_db.json")
User = Query()

class Player:
    def __init__(self,first_name, name, birthday,chess_id, db_id=None):
        self.first_name =first_name
        self.name = name
        self.birthday = birthday
        self.chess_id = chess_id
        self.db_id = db_id

    
    def __str__(self):
        """Used in print."""
        return f"{self.first_name} {self.name} {self.birthday} {self.chess_id}"
    
    def __repr__(self) -> str:
        """Used in print."""
        return str(self)
    
    def serialize(self):
       serialized_player ={
            "first_name":self.first_name,
            "name":self.name,
            "birthday":self.birthday,
            "chess_id": self.chess_id
        }
       return serialized_player
    
    def save(self):
        self.db_id = db.insert(self.serialize())
        return self.db_id
    
    #def update_player(self):
      # self.db_id = db.update({self.first_name: first_name})
    
    @classmethod 
    def get(cls, id):
      """Return a player object"""

      data = db.get(doc_id=id)
      if data is None:
          return None
      
      data["db_id"] = data.doc_id

      player = Player(**data)
      return player
    
    @classmethod
    def all(cls, type_player=False):
       """Return a list of players"""
       
       all_data = db.all()
       for player in all_data :
           player["db_id"] = player.doc_id
       if type_player == False:
           return all_data
       else:
            players = []
            for player_dict in all_data:
                #player = Player(**player_dict)
                players.append(Player(**player_dict))
            return players
          
    
    
    
if __name__=="__main__" :
    players = Player.getPlayer()
    print(players)
    
    
    

#class Tournemant:
    #def __init__(self, nom_tournois, lieu_tounois, debut_tournois, fin_tournois, nombre_tour, description_tour, round, status):
       # self.nom_tournois = nom_tournois
       # self.lieu_tournois = lieu_tounois
       # self.debut_tournois = debut_tournois
       # self.fin_tournois = fin_tournois
       # self.nombre_tour = nombre_tour
        #self.decription_tour = description_tour
        #self.round = round
        #self.ststus = status

    