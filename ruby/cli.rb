require 'thor'


class Cli < Thor
  desc "deploy APP", "make a app deploy"
  option :repo, :required => true, :default => "https://..."
  def deploy(app)
    puts "Fazendo deploy #{app}"
    puts "Repo Name: #{options[:repo]}" if options[:repo]
  end


end

Cli.start(ARGV)

