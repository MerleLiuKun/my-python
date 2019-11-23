"""
    基础的数据类实现
"""
from dataclasses import dataclass, field


@dataclass
class Page:
    id: str = None
    about: str = field(default=None, repr=False)
    birthday: str = field(default=None, repr=False)
    name: str = None
    username: str = None
    fan_count: int = field(default=None, repr=False)
    cover: dict = field(default=None, repr=False)


if __name__ == '__main__':
    data = {
        "id": "20531316728",
        "about": "The Facebook Page celebrates how our friends inspire us, support us, and help us discover the world when we connect.",
        "birthday": "02/04/2004",
        "name": "Facebook",
        "username": "facebookapp",
        "fan_count": 214643503,
        "cover": {
            "cover_id": "10158913960541729",
            "offset_x": 50,
            "offset_y": 50,
            "source": "https://scontent.xx.fbcdn.net/v/t1.0-9/s720x720/73087560_10158913960546729_8876113648821469184_o.jpg?_nc_cat=1&_nc_ohc=bAJ1yh0abN4AQkSOGhMpytya2quC_uS0j0BF-XEVlRlgwTfzkL_F0fojQ&_nc_ht=scontent.xx&oh=2964a1a64b6b474e64b06bdb568684da&oe=5E454425",
            "id": "10158913960541729"
        }
    }
    # 数据加载
    p = Page(**data)

    print(p.name)
    print(p)
    print(p.cover)
