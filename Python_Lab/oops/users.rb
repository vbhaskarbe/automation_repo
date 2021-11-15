
class Users
        attr_accessor :name, :password, :sname

        def initialize(name, password, sname)
          self.name = name
          self.password = password
          self.sname = sname
        end
        
        def display()
          puts "User is #{self.name}, Password is #{self.password}"
        end
        
end

rootuser = Users.new( 'admin@cliqrtech.com', 'cliqr', '')
rootuser.display
tenantuser = rootuser
tenantuser.display
testuser   = tenantuser
testuser.display
puts rootuser.name


