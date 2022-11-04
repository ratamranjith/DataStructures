# Search an element in an unsorted array
a = [25, 34, 45, 5, 67]

def search_element(arr, searchValue)
	elementIndex = nil
	begin
	(arr.length).times do |element|
		if(arr[element].eql? searchValue)
			elementIndex = element
			break
		end
	end
	rescue
		p "something went wrong"
	ensure
		return elementIndex
	end
end

# Linear Search - Time Complexity : O(n)
search_element(a, 5)
