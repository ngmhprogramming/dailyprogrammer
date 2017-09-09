def details()
    print("What is your name?")
    name = gets.chomp
    print("What is your age?")
    age = gets.chomp
    print("What is your reddit username?")
    username = gets.chomp
    open("ruby_easy_1_details.txt", 'a') do |file|
        file.print("#{name} \n")
        file.print("#{age} \n")
        file.print("#{username}\n")
    end
end

if __FILE__ == $0
    details()
end