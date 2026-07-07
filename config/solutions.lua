-- solutions.lua
--
-- Toggles the visibility of "solution" content depending on the
-- `show-solutions` document metadata (set by make_pdf.py).
--
-- Two kinds of solutions are recognised:
--   1. Inline / display math of the form  \color{blue}{ ... }
--      In "questions" mode each such group is replaced by \phantom{ ... }
--      so the layout is preserved and an empty space of the same size is
--      left for the student to fill in. In "solutions" mode it is kept as
--      the original blue formula.
--   2. Pandoc Divs with the class "solution" (::: solution ... :::) are
--      dropped entirely in "questions" mode and kept in "solutions" mode.

local MARKER = "\\color{blue}"

-- Replace every balanced \color{blue}{ ... } group in a raw (La)TeX math
-- string with \phantom{ ... }. Brace matching is escape-aware so that
-- literal braces such as \} (e.g. inside \left. ... \right\}) are ignored.
local function hide_color(text)
  local out = {}
  local i = 1
  local n = #text
  local mlen = #MARKER

  while i <= n do
    local s = text:find(MARKER, i, true)
    if not s then
      out[#out + 1] = text:sub(i)
      break
    end

    -- copy everything before the marker verbatim
    out[#out + 1] = text:sub(i, s - 1)

    -- position just after "\color{blue}", skipping any whitespace
    local j = s + mlen
    while j <= n and text:sub(j, j):match("%s") do
      j = j + 1
    end

    if text:sub(j, j) == "{" then
      -- walk forward to the matching closing brace
      local depth = 0
      local k = j
      while k <= n do
        local c = text:sub(k, k)
        if c == "\\" then
          k = k + 2                -- skip escaped char (\{ \} \\ ...)
        elseif c == "{" then
          depth = depth + 1
          k = k + 1
        elseif c == "}" then
          depth = depth - 1
          if depth == 0 then break end
          k = k + 1
        else
          k = k + 1
        end
      end

      local content = text:sub(j + 1, k - 1)
      -- recurse in case of (unlikely) nested \color{blue}{...}
      out[#out + 1] = "\\phantom{" .. hide_color(content) .. "}"
      i = k + 1
    else
      -- a bare \color{blue} switch (no braces) -- leave it untouched
      out[#out + 1] = MARKER
      i = s + mlen
    end
  end

  return table.concat(out)
end

local function has_class(el, class)
  if not el.classes then return false end
  for _, c in ipairs(el.classes) do
    if c == class then return true end
  end
  return false
end

function Pandoc(doc)
  local show = false
  local v = doc.meta["show-solutions"]

  if v ~= nil then
    if type(v) == "boolean" then
      show = v
    elseif type(v) == "string" then
      show = (v:lower() == "true")
    else
      -- pandoc MetaValue (e.g. MetaInlines) -> stringify
      show = (pandoc.utils.stringify(v):lower() == "true")
    end
  end

  io.stderr:write("DEBUG: show-solutions = " .. tostring(show) .. "\n")

  local function handle_math(m)
    if not show then
      m.text = hide_color(m.text)
      return m
    end
  end

  local function handle_div(div)
    if has_class(div, "solution") then
      return show and div or {}
    end
  end

  return doc:walk{ Math = handle_math, Div = handle_div }
end
