
class GoodDog
        def initialize(name)
          @name = name
        end

        def speak
          "Arf!"
        end

        def speak2
          "#{@name} says Arf!"
        end

        def get_name
          @name
        end

        def set_name=(name)
          @name = name
        end

        def name
          @name
        end

        def name=(name)
          @name = name
        end
end

sparky = GoodDog.new('Sparky')
fido = GoodDog.new("Fido")
puts sparky.speak
puts fido.speak 
puts sparky.speak2
puts fido.speak2
puts sparky.get_name
sparky.set_name = "Spartacus"
puts sparky.get_name
puts sparky.name  
sparky.name = "Spartacus2"
puts sparky.name
