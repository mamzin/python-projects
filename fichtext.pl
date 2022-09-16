#!/usr/bin/perl
#avmamzin

while ($key != 3)
{
	&printmenu;
	$key = <STDIN>;
	if ($key == 1)
	{
		print "Where to search?\n";
		chomp ($gde = <STDIN>);
		print "Which text for search?\n";
		chomp ($chto = <STDIN>);
		@list = &get_files($gde);
		foreach $i (@list)
		{
			open (TEMPFILE, $i) || die "Can not open $i: $!\n"; 
			while (<TEMPFILE>)
			{
				if (/$chto/)
				{
					print "*****FOUND TEXT IN FILE: $i AT LINE:\n";
					print;
				}
			}
			close TEMPFILE;
		}
		print "\n";
	}
	elsif ($key == 2)
	{
		print "WARNING! NOT TO USE THE SYSTEM FOLDERS!\n";
		print "Where to search?\n";
		chomp ($gde = <STDIN>);
		print "Which text for change?\n";
		chomp ($chto = <STDIN>);
		print "Which new text?\n";
		chomp ($newt = <STDIN>);
		@list = &get_files($gde);
		foreach $i (@list)
		{
			system("/usr/bin/sed -e 's/$chto/$newt/g' $i > $i.t");
			system("mv $i.t $i");	
			print "*****TEXT IS REPLACED IN FILE: $i\n";
		}
	}
}

sub get_files
{
	my @dir = $_[0];
	my @files;
	while ($file = shift @dir)
	{
		opendir (DIR, $file) || die "Can not open $file: $!\n";
		while ($rd = readdir DIR)
		{
			if (-f "$file/$rd")
			{
				$node = "$file/$rd";
				push @files, $node;
			}
			elsif (($rd != ".") && ($rd != ".."))
			{
				push @dir, "$file/$rd";
			}
		}
	}
	closedir DIR;
	return @files;
}

sub printmenu {
	print "Select Your choice [1-3]:\n";
	print "1 - Find files with text\n";
	print "2 - Replace text in files\n";
	print "3 - Exit\n";
}
