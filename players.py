from tinydb import TinyDB, Query

db = TinyDB("player_db.json")
User = Query()

class Player:
    def __init__(self,first_name, name, birthday,chess_id, db_id=None):
        self.first_name =first_name
        self.name = name
        self.birthday = birthday
        self.chess_id = chess_id
        self.db_id = db_id

    
    def __str__(self):
        return f"{self.first_name} {self.name} {self.birthday} {self.chess_id}"
    
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
      data = db.get(doc_id=id)
      if data is None:
          return None
      
      player = Player(**data)
      return player
    
    @classmethod
    def all(cls, doc_ids):
        all_data = db.all(doc_ids)
        all_data_p = Player(**all_data)
        return all_data_p
        
    
    

    
    
if __name__=="__main__" :
   print(Player.all(1))
    
    
    

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

    