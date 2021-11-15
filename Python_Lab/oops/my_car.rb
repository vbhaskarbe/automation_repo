
class MyCar
        attr_accessor :year, :color, :model

        def initialize( y, c, m)
          self.year = y
          self.color = c
          self.model = m
          @current_speed = 0
        end

        def speedup(kmph = 20)
          @current_speed += kmph
          puts "You have accelarated to #{@current_speed}"
        end

        def brake(kmph = 20)
          @current_speed -= kmph
          puts "You have slowed down to #{@current_speed}"
        end

        def shutoff()
          @current_speed = 0
          puts "Engine is off"
        end

        def showspeed()
          puts "Your current speed is #{@current_speed}"
          puts self.what_am_i
        end

end

figo = MyCar.new('2014', 'Mars Red', 'Ford')
figo.showspeed
figo.speedup
figo.speedup
figo.brake
figo.shutoff
figo.showspeed

