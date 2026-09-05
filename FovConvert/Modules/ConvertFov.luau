local module = {}

function module:Convert(keyframelist)
	
	local CoreFolder = Instance.new("Folder")
	CoreFolder.Name = "FieldOfView"
	
	local firstframe = Instance.new("Folder", CoreFolder)
	firstframe.Name = "0"
	
	local default = Instance.new("NumberValue", CoreFolder)
	default.Name = "default"
	default.Value = 70
	
	local frames = Instance.new("Folder", firstframe)
	frames.Name = "Values"
	
	for i, v in ipairs(keyframelist) do
		local frm = Instance.new("NumberValue", frames)
		frm.Name = i - 1
		frm.Value = v
	end
	
	return CoreFolder
	
end

return module
