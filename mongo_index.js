db.PROFISSIONAL.createIndex({"email":1}, {background:true, unique:true})
db.PROFISSIONAL.createIndex({"usuario":1}, {background:true, unique:true})
db.CLIENTE.createIndex({"email":1}, {background:true, unique:true})
db.CLIENTE.createIndex({"usuario":1}, {background:true, unique:true})