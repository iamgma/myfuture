Sub Reset_Button():

  ' Pass the previous grade to the Last Grade row
  Cells(12, 2).Value = Cells(2, 2).Value
  Cells(12, 3).Value = Cells(2, 3).Value
  Cells(12, 4).Value = Cells(2, 4).Value

  ' Empty out the current grade and remember to set the colour back to default
  Cells(2, 2).Value = ""
  Cells(2, 3).Value = ""
  Cells(2, 3).Interior.ColorIndex = 0
  Cells(2, 4).Value = ""

End Sub
