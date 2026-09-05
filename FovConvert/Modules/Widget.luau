local _s = _G.ShakyGlobal

local plugin = _s.Plugin

local module = {
	Widget = _s.FOVWidget
}

function module.GetWidget(self)
	
	local wdgt = _s.FOVWidget
	
	return _s.FOVWidget
	
end

function module.Create(self)
	
	local Widget
	
	if _s.RefreshState == 0 then
	
		Widget = plugin:CreateDockWidgetPluginGuiAsync("TestWidget2232133", DockWidgetPluginGuiInfo.new(
			Enum.InitialDockState.Float,
			true,
			false,
			200,
			300,
			150,
			150
			))
		_s.FOVWidget = Widget
	
		Widget.Title = "Test Widget"  -- Optional widget title
		
		self.Widget = Widget
		
	else
		
		Widget = self.Widget
		
	end
	
	local ui = script:WaitForChild("CoreUI")

	Widget:ClearAllChildren()

	ui:Clone().Parent = self.Widget
	
	_s.RefreshState = 2
	
	return _s.FOVWidget
	
end

function module.Toggle(self)
	
	local wdgt = self:GetWidget()
	
	if not wdgt or _s.RefreshState == 1 then
		self:Create()
	end
	
	return wdgt
	
end

return module
