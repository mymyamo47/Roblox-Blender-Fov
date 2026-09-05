local RunService = game:GetService("RunService")
local selection = game:GetService("Selection")
local ScriptEditorService = game:GetService("ScriptEditorService")

local _g = nil
local isNewInstance = true

if not _G.ShakyGlobal then

	if RunService:IsRunMode() or RunService:IsRunning() then
		return
	end

	local attempts = 0

	repeat
		_g = _G.MoonGlobal

		task.wait(1)
	until (_g and _g.ready) or attempts > 150
	
else
	
	_g = _G.MoonGlobal
	
end

_G.ShakyGlobal = _G.ShakyGlobal or {}

local _s = _G.ShakyGlobal

_s.Plugin = plugin

local Widget = require(script.Parent.Modules.Widget)
local ConvertFOV = require(script.Parent.Modules.ConvertFov)

local Button = _s.Button

if not Button then

	Button = _g.toolbar:CreateButton("Convert FOV", "", "rbxassetid://5428197036")
	
	_s.Button = Button
end

if _s.RefreshState == nil then
	_s.RefreshState = 0
else
	_s.RefreshState = 1
end
-- 0 = first time, 1 = refreshed, 2 = finished

local onclick = function()
	
	local clipboardkeyframes = Instance.new("Script")
	clipboardkeyframes.Parent = workspace
	
	local message = "-- Paste compiled keyframes here\n"
	
	clipboardkeyframes.Source = message
	
	_s.clipboardevent = ScriptEditorService.TextDocumentDidChange:Connect(function(myscript, changes)
		if myscript == ScriptEditorService:FindScriptDocument(clipboardkeyframes) then
			_s.clipboardevent:Disconnect()
			
			local code = clipboardkeyframes.Source
			
			local keyframes = ConvertFOV:Convert(code:sub(#message+1):split(", "))
			
			local cutscene = selection:Get()[1]
			
			local camerafound = false
			
			if cutscene then

				for i, v in ipairs(cutscene:GetChildren()) do
					if not camerafound then
						if v:FindFirstChild("FieldOfView") then
							camerafound = v
							print("Camera found!", v)
						end
					else
						break
					end
				end
				
			end
			
			if camerafound then
				
				camerafound:FindFirstChild("FieldOfView"):Remove()
				keyframes.Parent = camerafound
				
			else
				
				keyframes.Parent = workspace
				
			end
			
			clipboardkeyframes:Remove()
		end
	end)
	
	plugin:OpenScript(clipboardkeyframes, 2)
	
end

if _s.OnClickEvent then
	_s.OnClickEvent:Disconnect()
end

_s.OnClickEvent = Button.Click:Connect(onclick)