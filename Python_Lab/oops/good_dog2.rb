
class GoodDog2
        attr_accessor :name

        def initialize(name = 'default')
          @name = name
        end

        def speak
          "#{name} says arf!"
        end
end

sparky = GoodDog2.new()
puts sparky.speak
puts sparky.name
sparky = GoodDog2.new('Sparky')
puts sparky.speak
puts sparky.name


