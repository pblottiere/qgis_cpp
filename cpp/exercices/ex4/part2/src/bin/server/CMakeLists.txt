SET(SOURCES
  main.cpp)

SET(MYLIB_HEADERS
  ${MYLIB_DIR}/net/client.h
  ${MYLIB_DIR}/net/server.h)

INCLUDE(${QT_USE_FILE})
ADD_DEFINITIONS(${QT_DEFINITIONS})

INCLUDE_DIRECTORIES(${MYLIB_DIR})
INCLUDE_DIRECTORIES(${QGIS_INCLUDE_DIR})
INCLUDE_DIRECTORIES(${QT_INCLUDE_DIR}/QtXml)

QT4_WRAP_CPP(MYLIB_MOC ${MYLIB_HEADERS})

ADD_EXECUTABLE(server ${SOURCES} ${MYLIB_MOC})
TARGET_LINK_LIBRARIES(server ${QT_LIBRARIES})
TARGET_LINK_LIBRARIES(server qgis_core)
TARGET_LINK_LIBRARIES(server qgis_gui)
TARGET_LINK_LIBRARIES(server qgis_app)
TARGET_LINK_LIBRARIES(server QtNetwork)
TARGET_LINK_LIBRARIES(server net)
